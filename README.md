## Desarrollo de APIs con FastAPI en Python

## Descripción del Proyecto
Este proyecto consiste en una aplicación web construida con FastAPI, un marco de trabajo de Python para construir APIs web rápidas. La aplicación proporciona endpoints para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en una base de datos MySQL.

#### Estructura de Carpetas
- Scripts: Contiene el script SQL utilizado para crear la tabla en la base de datos MySQL.
- Static/Css: Contiene los archivos CSS de Bootstrap utilizados para dar estilo a la interfaz de usuario de la aplicación.
- Templates: Aquí se encuentran los archivos HTML que se utilizan para la interfaz de usuario de la aplicación. Estos archivos HTML renderizan la salida de las API creadas con FastAPI.
- Venv: Este directorio contiene el entorno virtual de Python utilizado para aislar las dependencias del proyecto.
- app.py: Este archivo contiene toda la lógica implementada para las API, incluyendo los métodos GET, POST, PUT y DELETE para interactuar con la base de datos y manejar las solicitudes de los clientes.
- requirements.txt contiene una lista de todas las dependencias y versiones de Python necesarias para ejecutar la aplicación. Estas dependencias se instalan automáticamente utilizando la herramienta pip, lo que facilita la configuración del entorno de desarrollo.

[![estructura.png](https://i.postimg.cc/25d85r4V/estructura.png)](https://postimg.cc/jW5rgV3b)

#### Interfaz de Usuario
Para mejorar la experiencia visual, se ha implementado una página HTML utilizando el framework Bootstrap. Esta página proporciona una interfaz intuitiva para interactuar con las API proporcionadas por la aplicación.

#### Instrucciones para Configurar el Entorno del Proyecto

1.- Clonar el Repositorio:

Clona este repositorio en tu máquina local utilizando el siguiente comando:

	git clone <url_del_repositorio>

2.- Configurar la Base de Datos:

- Abre tu cliente de MySQL u otro cliente SQL de tu elección.
- Utiliza el cliente para cargar el script script.sql y crear las tablas en la base de datos. Puedes abrir el archivo en el cliente y ejecutarlo directamente.
- Una vez creadas la tabla, carga el archivo querys.sql en tu cliente SQL para agregar datos a la base de datos.

3.- Activar el Entorno Virtual:

Activa el entorno virtual del proyecto utilizando el siguiente comando:

	source venv/bin/activate
	
4.- Instalar Dependencias:

Instala las dependencias del proyecto desde el archivo requirements.txt utilizando el siguiente comando:

	pip install -r requirements.txt
	
5.- Ejecutar la Aplicación:

Ejecuta el archivo app.py para iniciar la aplicación FastAPI. Utiliza el siguiente comando:

	uvicorn app:app --reload

#### Capturas de Código Python:

[![python1.png](https://i.postimg.cc/PrkBJ6Zr/python1.png)](https://postimg.cc/vD3PSt3p)

#### Método Get
[![python2-get.png](https://i.postimg.cc/sXC5RZQx/python2-get.png)](https://postimg.cc/7CX53hNr)
#### Método Post
[![python2-post.png](https://i.postimg.cc/nVyGJz56/python2-post.png)](https://postimg.cc/nM1DKHnk)
#### Método Put
[![python2-put.png](https://i.postimg.cc/766rwXCY/python2-put.png)](https://postimg.cc/ns6P14Y6)
#### Método Delete
[![python2-delete.png](https://i.postimg.cc/g0p6SLxK/python2-delete.png)](https://postimg.cc/sMnX1X9B)
#### Captura de Página HTML
[![captura-pagina-html.png](https://i.postimg.cc/rm8wBv2d/captura-pagina-html.png)](https://postimg.cc/FfBvcCRm)
#### Captura de un nuevo registro
[![nuevo-registro.png](https://i.postimg.cc/cLqyW7QQ/nuevo-registro.png)](https://postimg.cc/RNTbQHpF)

[![lista-registro.png](https://i.postimg.cc/yNc05K7m/lista-registro.png)](https://postimg.cc/CZMZBWB5)

#### Captura de actualización de un registro
[![editar-registro.png](https://i.postimg.cc/MK0qShfm/editar-registro.png)](https://postimg.cc/zVf9w2jy)

#### Captura de eliminar un registro
[![delete-registro.png](https://i.postimg.cc/Qx2nBQKg/delete-registro.png)](https://postimg.cc/vcvvk6zD)

[![delete-registro-resultado.png](https://i.postimg.cc/yxzy1PbW/delete-registro-resultado.png)](https://postimg.cc/MMdQtyx8)
