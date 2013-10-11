# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd.
# License: GNU General Public License v3. See license.txt

# SETUP:
# install pip install --upgrade google-api-python-client
#
# In Google API
# - create new API project
# - create new oauth2 client (create installed app type as google \
# 	does not support subdomains)
#
# in conf.py, set oauth2 settings
# gdrive_client_id
# gdrive_client_secret

from __future__ import unicode_literals
import httplib2
import os
import mimetypes
import webnotes
import oauth2client.client
from webnotes.utils import get_base_path, cstr
from webnotes import _, msgprint
from apiclient.discovery import build
from apiclient.http import MediaFileUpload

# define log config for google drive api's log messages
# basicConfig redirects log to stderr
import logging
logging.basicConfig()

@webnotes.whitelist()
def get_gdrive_authorize_url():
	flow = get_gdrive_flow()
	authorize_url = flow.step1_get_authorize_url()
	return {
		"authorize_url": authorize_url,
	}

def upload_files(name, mimetype, service, folder_id):
	if not webnotes.conn:
		webnotes.connect()
	file_name = os.path.basename(name)
	media_body = MediaFileUpload(name, mimetype=mimetype, resumable=True)
	body = {
		'title': file_name,
		'description': 'Backup File',
		'mimetype': mimetype,
		'parents': [{
			'kind': 'drive#filelink',
			'id': folder_id
		}]
	}
	request = service.files().insert(body=body, media_body=media_body)
	response = None
	while response is None:
		status, response = request.next_chunk()

def backup_to_gdrive():
	from webnotes.utils.backups import new_backup
	if not webnotes.conn:
		webnotes.connect()
	get_gdrive_flow()
	credentials_json = webnotes.conn.get_value("Backup Manager", None, "gdrive_credentials")
	credentials = oauth2client.client.Credentials.new_from_json(credentials_json)
	http = httplib2.Http()
	http = credentials.authorize(http)
	drive_service = build('drive', 'v2', http=http)

	# upload database
	backup = new_backup()
	path = os.path.join(get_base_path(), "public", "backups")
	filename = os.path.join(path, os.path.basename(backup.backup_path_db))
	
	# upload files to database folder
	upload_files(filename, 'application/x-gzip', drive_service, 
		webnotes.conn.get_value("Backup Manager", None, "database_folder_id"))
	
	# upload files to files folder
	did_not_upload = []
	error_log = []
	
	files_folder_id = webnotes.conn.get_value("Backup Manager", None, "files_folder_id")
	
	webnotes.conn.close()
	path = os.path.join(get_base_path(), "public", "files")
	for filename in os.listdir(path):
		found = False
		filepath = os.path.join(path, filename)
		ext = filename.split('.')[-1]
		size = os.path.getsize(filepath)
		if ext == 'gz' or ext == 'gzip':
			mimetype = 'application/x-gzip'
		else:
			mimetype = mimetypes.types_map.get("." + ext) or "application/octet-stream"
		
		#Compare Local File with Server File
	  	children = drive_service.children().list(folderId=files_folder_id).execute()
	  	for child in children.get('items', []):
			file = drive_service.files().get(fileId=child['id']).execute()
			if filename == file['title'] and size == int(file['fileSize']):
				found = True
				break
		if not found:
			try:
				upload_files(filepath, mimetype, drive_service, files_folder_id)
			except Exception, e:
				did_not_upload.append(filename)
				error_log.append(cstr(e))
	
	webnotes.connect()
	return did_not_upload, list(set(error_log))

def get_gdrive_flow():
	from oauth2client.client import OAuth2WebServerFlow
	import conf
	
	if not hasattr(conf, "gdrive_client_id"):
		webnotes.msgprint(_("Please set Google Drive access keys in") + " conf.py", 
		raise_exception=True)

	flow = OAuth2WebServerFlow(conf.gdrive_client_id, conf.gdrive_client_secret, 
		"https://www.googleapis.com/auth/drive", 'urn:ietf:wg:oauth:2.0:oob')
	return flow
	
@webnotes.whitelist()
def gdrive_callback(verification_code = None):
	flow = get_gdrive_flow()
	if verification_code:
		credentials = flow.step2_exchange(verification_code)
		allowed = 1
		
	# make folders to save id
	http = httplib2.Http()
	http = credentials.authorize(http)
	drive_service = build('drive', 'v2', http=http)
	owrang_folder_id = create_owrang_folder(drive_service)
	database_folder_id = create_folder('database', drive_service, owrang_folder_id)
	files_folder_id = create_folder('files', drive_service, owrang_folder_id)

	webnotes.conn.set_value("Backup Manager", "Backup Manager", "gdrive_access_allowed", allowed)
	webnotes.conn.set_value("Backup Manager", "Backup Manager", "database_folder_id", database_folder_id)
	webnotes.conn.set_value("Backup Manager", "Backup Manager", "files_folder_id", files_folder_id)
	final_credentials = credentials.to_json()
	webnotes.conn.set_value("Backup Manager", "Backup Manager", "gdrive_credentials", final_credentials)

	webnotes.msgprint("Updated")

def create_owrang_folder(service):
	if not webnotes.conn:
		webnotes.connect()
	owrang = {
		'title': 'owrang',
		'mimeType': 'application/vnd.google-apps.folder'
	}
	owrang = service.files().insert(body=owrang).execute()
	return owrang['id']

def create_folder(name, service, folder_id):
	database = {
		'title': name,
		'mimeType': 'application/vnd.google-apps.folder',
		'parents': [{
	       	'kind': 'drive#fileLink',
	       	'id': folder_id
	    }]
	}
	database = service.files().insert(body=database).execute()
	return database['id']

if __name__=="__main__":
	backup_to_gdrive()