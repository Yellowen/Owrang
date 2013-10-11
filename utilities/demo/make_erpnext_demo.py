if __name__=="__main__":
	import sys
	sys.path.extend([".", "lib", "app"])

import webnotes, os
import utilities.demo.make_demo

def make_demo_app():
	webnotes.mute_emails = 1
	webnotes.connect()
	utilities.demo.make_demo.make(reset=True, simulate=False)
	# setup demo user etc so that the site it up faster, while the data loads
	make_demo_user()
	make_demo_login_page()
	make_demo_on_login_script()
	utilities.demo.make_demo.make(reset=False, simulate=True)

def make_demo_user():
	roles = ["Accounts Manager", "Analytics", "Expense Approver", "Accounts User", 
		"Leave Approver", "Blogger", "Customer", "Sales Manager", "Employee", "Support Manager", 
		"HR Manager", "HR User", "Maintenance Manager", "Maintenance User", "Material Manager", 
		"Material Master Manager", "Material User", "Manufacturing Manager", 
		"Manufacturing User", "Projects User", "Purchase Manager", "Purchase Master Manager", 
		"Purchase User", "Quality Manager", "Report Manager", "Sales Master Manager", 
		"Sales User", "Supplier", "Support Team"]
		
	def add_roles(bean):
		for role in roles:
			p.doclist.append({
				"doctype": "UserRole",
				"parentfield": "user_roles",
				"role": role
			})
	
	# make demo user
	if webnotes.conn.exists("Profile", "demo@owrang.yellowen.com"):
		webnotes.delete_doc("Profile", "demo@owrang.yellowen.com")

	p = webnotes.new_bean("Profile")
	p.doc.email = "demo@owrang.yellowen.com"
	p.doc.first_name = "Demo"
	p.doc.last_name = "User"
	p.doc.enabled = 1
	p.doc.user_type = "Owrang Demo"
	p.doc.send_invite_email = 0
	p.doc.new_password = "demo"
	p.insert()
	add_roles(p)
	p.save()
	
	# make system manager user
	if webnotes.conn.exists("Profile", "admin@owrang.yellowen.com"):
		webnotes.delete_doc("Profile", "admin@owrang.yellowen.com")
	
	p = webnotes.new_bean("Profile")
	p.doc.email = "admin@owrang.yellowen.com"
	p.doc.first_name = "Admin"
	p.doc.last_name = "User"
	p.doc.enabled = 1
	p.doc.user_type = "System User"
	p.doc.send_invite_email = 0
	p.doc.new_password = "admin010123"
	p.insert()
	roles.append("System Manager")
	add_roles(p)
	p.save()
	
	# only read for newsletter
	webnotes.conn.sql("""update `tabDocPerm` set `write`=0, `create`=0, `cancel`=0
		where parent='Newsletter'""")
	webnotes.conn.sql("""update `tabDocPerm` set `write`=0, `create`=0, `cancel`=0
		where parent='Profile' and role='All'""")
	
	webnotes.conn.commit()

def make_demo_login_page():
	webnotes.conn.set_value("Website Settings", None, "home_page", "")

	webnotes.conn.sql("""delete from `tabWeb Page` where name='demo-login'""")
	p = webnotes.new_bean("Web Page")
	p.doc.title = "Demo Login"
	p.doc.published = 1
	p.doc.description = "Owrang Demo Login"

	with open(os.path.join(os.path.dirname(__file__), "demo-login.html"), "r") as dfile:
		p.doc.main_section = dfile.read()

	p.doc.insert_code = 1
	with open(os.path.join(os.path.dirname(__file__), "demo-login.js"), "r") as dfile:
		p.doc.javascript = dfile.read()

	p.doc.insert_style = 1
	with open(os.path.join(os.path.dirname(__file__), "demo-login.css"), "r") as dfile:
		p.doc.css = dfile.read()
		
	p.insert()
	
	website_settings = webnotes.bean("Website Settings", "Website Settings")
	website_settings.doc.home_page = "demo-login"
	website_settings.doc.disable_signup = 1
	website_settings.save()
	
	webnotes.conn.commit()

def make_demo_on_login_script():
	webnotes.conn.sql("""delete from `tabCustom Script` where dt='Control Panel'""")
	s = webnotes.new_bean("Custom Script")
	s.doc.dt = "Control Panel"
	s.doc.script_type = "Server"
	with open(os.path.join(os.path.dirname(__file__), "demo_control_panel.py"), "r") as dfile:
		s.doc.script = dfile.read()
	s.insert()
	
	cp = webnotes.bean("Control Panel")
	cp.doc.custom_startup_code = """wn.ui.toolbar.show_banner('You are using Owrang Demo. To start your own Owrang Trial, <a href="https://owrang.yellowen.com/pricing-and-signup" target="_blank">click here</a>')"""
	cp.save()

	webnotes.conn.commit()

if __name__=="__main__":
	make_demo_app()