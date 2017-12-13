#-*-coding: utf-8 -*-
import sys,os
opcion1=sys.argv[1]
nombre=sys.argv[2]

if opcion1 == '-a':
        listad = open('/var/cache/bind/db.elultimohosting.com', 'a')
        listad.write(nombre+'   IN      CNAME   anakin''.elultimohosting.com.\n')
        listad.close()

elif opcion1 == '-b':
        os.system('sed -i /'+nombre+'/d /var/cache/bind/db.elultimohosting.com')

os.system('systemctl restart bind9')
