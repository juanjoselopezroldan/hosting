#-*-coding: utf-8 -*-
import MySQLdb as mariadb
import sys, commands

opcion=sys.argv[1]
usuario=sys.argv[2]


base='users'
usuadmin='root'
passadmin='root'

directorio='/srv/ftp/'+usuario

conectar= mariadb.connect("localhost",usuadmin,passadmin,base)
cursor= conectar.cursor()


if opcion == '-a':
	clave=sys.argv[3]
	uid=sys.argv[4]
	clavecifrada= commands.getoutput("echo "+clave+" | base64")
	
	cursor.execute("INSERT INTO usuario (nombre, clave, id, directorio) VALUES (%s,%s,%s,%s)",(usuario,clavecifrada,uid,directorio))

elif opcion == '-b':
	cursor.execute("DELETE FROM usuario WHERE nombre = '%s'"%usuario)
else:
	print 'La opcion indicada es erronea'

conectar.commit()
conectar.close()

print base
print usuario
print clave
print clavecifrada