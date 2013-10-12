---
{
	"_label": "How to Install Owrang",
	"_toc": [
		"docs.dev.install.restore_from_backup"
	]
}
---

> These are instructions that will help you to install Owrang on your Unix like system (Linux / Ubuntu / MacOS) using the Terminal. If you are looking at easier ways to evaluate Owrang, [see this page](docs.user.intro.try.html).

### Owrang Installer (Beta)

Install Owrang in one command!

1. Switch to root user using `sudo su`
1. Create a folder where you want to install erpnext
1. Go to the new folder
1. `wget https://raw.github.com/webnotes/erpnext/master/install_erpnext.py`
1. `python install_erpnext.py`

> If you are installing on your server for deployment, remember to change Administrator's password!

> If you get stuck, post your questions at [Owrang Developer Forum](https://groups.google.com/forum/#!forum/erpnext-developer-forum)

> [Troubleshooting SELinux](http://www.crypt.gen.nz/selinux/disable_selinux.html)

--

> [Server Setup Tips](http://plusbryan.com/my-first-5-minutes-on-a-server-or-essential-security-for-linux-servers)

> [MySQL configuration file - my.cnf](https://github.com/webnotes/erpnext/wiki/MySQL-configuration-file)

> [Some Useful Aliases](https://github.com/webnotes/erpnext/wiki/Some-Useful-Aliases)

---
### Upgrade / run latest patches

1. Backup your database!
1. Go to Setup > Update Owrang
1. Click on 'Update'