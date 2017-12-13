# hosting
Procedimientos para realizar la creación de un hosting con servicio web, ftp y base de datos.

Committeros: Manuel Franco, Maria Romero y Juan Jose Lopez

- [x] Instalación de Servidor Web.
- [x] Instalación de Servidor FTP.
- [x] Instalación de Servidor MariaDB.
- [x] Instalación de Servidor DNS.
- [ ] Autenticación con MariaDB.
- [ ] Instalación de PHPmyAdmin.
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
