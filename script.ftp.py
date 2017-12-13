#-*-coding: utf-8 -*-
import MySQLdb as mariadb
import sys

base='PREGUNTAR'
usuario=sys.argv[1]
clave=sys.argv[2]

usuadmin='PREGUNTAR'
passadmin='PREGUNTAR'

directorio='/srv/ftp/'+usuario

conectar= mariadb.connect("localhost",usuadmin,passadmin,base)

