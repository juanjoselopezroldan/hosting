#-*-coding: utf-8 -*-
import MySQLdb as mariadb
import sys, os

base=sys.argv[1]
usuario=sys.argv[1]
clave=sys.argv[2]

usuadmin='root'
passadmin='root'

directorio='/srv/ftp/'+usuario

os.system("mariadb -u "+usuadmin+" -p"+passadmin" -e 'create user "+usuario+"@'%' identified by "+clave+";'")
os.system("mariadb -u "+usuadmin+" -p"+passadmin" -e 'create database "+base+";'")
os.system("mariadb -u "+usuadmin+" -p"+passadmin" -e 'grant all privileges on "+base+".* to "+usuario+"@'%' identified by "+clave+";'")

os.system("mkdir "+directorio)

