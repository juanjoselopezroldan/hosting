# hosting
Procedimientos para realizar la creación de un hosting con servicio web, ftp y base de datos.

Committeros: Manuel Franco, Maria Romero y Juan Jose Lopez

- [x] Instalación de Servidor Web.
- [x] Instalación de Servidor FTP.
- [x] Instalación de Servidor MariaDB.
- [x] Instalación de Servidor DNS.
- [ ] Autenticación con MariaDB.
- [x] Instalación de PHPmyAdmin.
- [ ] Creación de Aplicación Web.
- [ ] Cuotas con volúmenes lógicos.
- [ ] Gestor Grafico FTP net2ftp.
- [ ] Estadísticas Web con awstat.
- [ ] Subir ficheros mediante repositorio gitHub.
- [ ] Creación de script de Alta/Baja de usuario y cambio de contraseña.


Se realizará en un entorno de prueba para depurar su funcionamiento y acto seguido se trasladará a un entorno de producción.

- En el entorno de prueba se realizará en una máquina.

	- Máquina 1 (Anakin "172.22.200.111"): Tendrá instalado todos los servicios.

- En el entorno de producción se realizara en dos máquinas, en las cuales los servicios se dividiran de la siguiente forma:

	- Máquina Obi-Wan: Tendrá los servicios de cara al exterior como el servidor web, el ftp o el servidor DNS.
	- Máquina Yoda: Tendrá la base de datos en la red interna, está no será accesible desde el exterior.


# Instalación del servidor Apache2:

`apt install apache2`

Una vez tengamos instalado Apache2, vamos a configurar la automatización de creación de virtualhost en apache2, esto se hará de la siguiente manera:


Tendremos un proceso que estará mirando a la carpeta donde se subirán los archivos por FTP y cuando tengamos una nueva carpeta con el nombre de usuario se creará automáticamente.

# mariaDB
## Instalación
`apt install mariadb-server`

## Configuración
Para crear un usuario y no tener que usar siempre root, nos conectamos con este usuario y creamos el nuevo:

~~~
MariaDB [(none)]> g
mysql -u root -p
MariaDB [(none)]> grant all privileges on *.* to 'auth'@'localhost' identified by '*****' with grant option;
~~~

Lo siguiente es crear la base de datos, las tablas e insertar datos:
~~~
mysql -u auth -p
MariaDB [(none)]> create database users
MariaDB [(none)]> use users
MariaDB [users]> create table testusers
    -> (
    -> username char(20) NOT NULL,
    -> password char(70) NOT NULL,
    -> email char(70)
    -> );
MariaDB [users]> insert into testusers values('maria.romero', '****', 'm.romeroangulo@gmail.com')`
~~~

# phpMyAdmin
## Instalación
`apt install phpmyadmin`

Durante la instalación nos da la opción de instalarlo en el momento o luego manualmente. La primera opción es la más cómoda si ya tenemos configurado todo lo de mariaDB. Nos pide una clave para el usuario administrador de phoMyAdmin y si queremos que vaya sobre apache o httpd.

## Configuración
Lo primero es deshabilitar el sitio por defecto que trae apache2:
`a2dissite 000-default`

Ahora creamos el virtual host para phpMyAdmin:
~~~
cd /etc/apache2/sites-availables
nano phpmyadmin.conf
<VirtualHost *:80>
        ServerName mysql.elultimohosting.com

        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html/
        RedirectMatch permanent ^/$ "/phpmyadmin/"

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined

</VirtualHost>
~~~

Se ha puesto un redirect para que cuando entremos en el sitio, vaya directamente a phpMyAdmin.
Una vez creado el fichero hay que habilitar el sitio
`a2ensite phpmyadmin.conf`

