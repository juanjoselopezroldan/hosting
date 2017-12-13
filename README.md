# hosting
Procedimientos para realizar la creación de un hosting con servicio web, ftp y base de datos.

Committeros: Manuel Franco, Maria Romero y Juan Jose Lopez

- [x] Instalación de Servidor Web.
- [ ] Instalación de Servidor FTP.
- [ ] Instalación de Servidor MariaDB.
- [ ] Instalación de Servidor DNS.
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


