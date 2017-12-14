#-*-coding: utf-8 -*-
import MySQLdb as mariadb
import sys, commands

opcion=sys.argv[1]
base='usuario'
usuario=sys.argv[2]
clave=sys.argv[3]
uid=sys.argv[4]
clavecifrada= commands.getoutput("echo "+clave+" | base64")


usuadmin='root'
passadmin='root'

directorio='/srv/ftp/'+usuario

conectar= mariadb.connect("localhost",usuadmin,passadmin,base)
cursor= conectar.cursor()

if opcion == '-a':
	cursor.execute("INSERT INTO ftpuser (nombre, clave, id, directorio) VALUES (\'" + nombre + "\',\'" + clavecifrada + "\'," + str(uid) + ",\'" + directorio +"\')")
elif opcion == '-b':
