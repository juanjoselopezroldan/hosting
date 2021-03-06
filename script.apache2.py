#-*-coding: utf-8 -*-
import sys, os

opcion=sys.argv[1]
usuario=sys.argv[2]

virtualhost=["<VirtualHost *:80> \n",
	"# The ServerName directive sets the request scheme, hostname and port that \n",
	"# the server uses to identify itself. This is used when creating \n",
	"# redirection URLs. In the context of virtual hosts, the ServerName \n",
	"# specifies what hostname must appear in the request's Host: header to \n",
	"# match this virtual host. For the default virtual host (this file) this \n",
	"# value is not decisive as it is used as a last resort host regardless. \n",
	"# However, you must set it for any further virtual host explicitly. \n",
	"ServerName "+usuario+".elultimohosting.com \n",

	"ServerAdmin webmaster@localhost \n",
	"DocumentRoot /srv/ftp/"+usuario+" \n",

	"# Available loglevels: trace8, ..., trace1, debug, info, notice, warn, \n",
	"# error, crit, alert, emerg. \n",
	"# It is also possible to configure the loglevel for particular \n",
	"# modules, e.g. \n",
	"#LogLevel info ssl:warn \n",

	"ErrorLog ${APACHE_LOG_DIR}/"+usuario+"/error.log \n",
	"CustomLog ${APACHE_LOG_DIR}/"+usuario+"/access.log combined \n",

	"# For most configuration files from conf-available/, which are \n",
	"# enabled or disabled at a global level, it is possible to \n",
	"# include a line for only one particular virtual host. For example the \n",
	"# following line enables the CGI configuration for this host only \n",
	"# after it has been globally disabled with "'a2disconf'". \n",
	"#Include conf-available/serve-cgi-bin.conf \n",
"</VirtualHost> \n",
"# vim: syntax=apache ts=4 sw=4 sts=4 sr noet \n"]

if opcion == '-a':
    os.system("chown www-data. /srv/ftp/"+usuario)
    os.system("mkdir /var/log/apache2/"+usuario)
    os.system("touch /var/log/apache2/"+usuario+"/error.log")
    os.system("touch /var/log/apache2/"+usuario+"/access.log")
	os.system("chown root:adm /var/log/apache2/"+usuario+" *")
	os.system("touch /etc/apache2/sites-available/"+usuario+".conf")
	datos=open('/etc/apache2/sites-available/'+usuario+'.conf',"a")
	datos.writelines(virtualhost)
	datos.close()
	os.system("a2ensite "+usuario+".conf")
	os.system("touch /srv/ftp/"+usuario+"/index.html")
	os.system("echo 'Sitio Creado Correctamente' > /srv/ftp/"+usuario+"/index.html")

elif opcion == '-b':
	os.system("a2dissite "+usuario+".conf")
	os.system("rm -rf /var/log/apache2/"+usuario)
	os.system("rm -rf /etc/apache2/sites-available/"+usuario+".conf")
	os.system("rm -rf /srv/ftp/"+usuario)

os.system("service apache2 restart")
os.system("service proftpd restart")
