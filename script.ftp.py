#-*-coding: utf-8 -*-
import MySQLdb as mariadb
import sys, commands

opcion=sys.argv[1]
base='users'
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
	cursor.execute("INSERT INTO usuario (nombre, clave, id, directorio) VALUES (\'" + usuario + "\',\'" + clavecifrada + "\'," + str(uid) + ",\'" + directorio +"\')")
elif opcion == '-b':
	cursor.execute("DELETE FROM usuario WHERE nombre = '%s'"%usuario)

print base
print usuario
print clave
print clavecifrada