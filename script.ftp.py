#-*-coding: utf-8 -*-
import MySQLdb as mariadb
import sys, os

base='usuarios'
usuario=sys.argv[1]
clave=sys.argv[2]
clavecifrada=os.system("echo "+clave+" | base64")

usuadmin='root'
passadmin='root'

directorio='/srv/ftp/'+usuario

#conectar= mariadb.connect("localhost",usuadmin,passadmin,base)

