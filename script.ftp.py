#-*-coding: utf-8 -*-
import MySQLdb as mariadb
import sys, os

base=sys.argv[1]
usuario=sys.argv[1]
clave=sys.argv[2]

usuadmin='root'
passadmin='root'

directorio='/srv/ftp/'+usuario


