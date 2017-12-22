#-*-coding: utf-8 -*-
import sys, os

opcion=sys.argv[1]
nombreweb=sys.argv[2]

virtualhost=["<VirtualHost *:80> \n"
	"# The ServerName directive sets the request scheme, hostname and port that \n"
	"# the server uses to identify itself. This is used when creating \n"
	"# redirection URLs. In the context of virtual hosts, the ServerName \n"
	"# specifies what hostname must appear in the request's Host: header to \n"
	"# match this virtual host. For the default virtual host (this file) this \n"
	"# value is not decisive as it is used as a last resort host regardless. \n"
	"# However, you must set it for any further virtual host explicitly. \n"
	"#ServerName "+nombreweb+" \n"

	"ServerAdmin webmaster@localhost \n"
	"DocumentRoot /var/www/"+nombreweb+" \n"

	"# Available loglevels: trace8, ..., trace1, debug, info, notice, warn, \n"
	"# error, crit, alert, emerg. \n"
	"# It is also possible to configure the loglevel for particular \n"
	"# modules, e.g. \n"
	"#LogLevel info ssl:warn \n"

	"ErrorLog ${APACHE_LOG_DIR}/"+nombreweb+"/error.log \n"
	"CustomLog ${APACHE_LOG_DIR}/"+nombreweb"/access.log combined \n"

	"# For most configuration files from conf-available/, which are \n"
	"# enabled or disabled at a global level, it is possible to \n"
	"# include a line for only one particular virtual host. For example the \n"
	"# following line enables the CGI configuration for this host only \n"
	"# after it has been globally disabled with "'a2disconf'". \n"
	"#Include conf-available/serve-cgi-bin.conf \n"
"</VirtualHost> \n"
"# vim: syntax=apache ts=4 sw=4 sts=4 sr noet \n"]

if opcion == '-a':
    os.system("mkdir /var/www"+nombreweb)
    os.system("chown www-data. /var/www/"+nombreweb)


elif opcion == '-b':
