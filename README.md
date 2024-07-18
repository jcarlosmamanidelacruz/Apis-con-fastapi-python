## Desarrollo de APIs con FastAPI en Python
<br><img src="https://i.postimg.cc/rsbMdzYW/apis-fastapi-python.png" alt="">

## Descripción del Proyecto
Este proyecto consiste en una aplicación web construida con FastAPI, un marco de trabajo de Python para construir APIs web rápidas. La aplicación proporciona endpoints para realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en una base de datos MySQL.

#### Importancia de una API

Las APIs (Interfaces de Programación de Aplicaciones) son fundamentales en el desarrollo de software moderno porque permiten la comunicación entre diferentes aplicaciones y servicios de manera eficiente y estandarizada. Facilitan la integración y la interoperabilidad entre sistemas diversos, permitiendo a los desarrolladores construir aplicaciones más complejas y funcionales reutilizando componentes existentes.

#### Endpoints Utilizados en el Proyecto

La aplicación web presenta una interfaz de usuario construida con HTML y estilizada con Bootstrap. Esta interfaz permite a los usuarios interactuar con las APIs de manera intuitiva, proporcionando varios endpoints para realizar operaciones CRUD en la base de datos MySQL. Estos endpoints son gestionados por FastAPI, que se encarga de recibir las solicitudes HTTP, procesarlas y devolver las respuestas adecuadas.

- GET /items: Recupera una lista de todos los registros de la base de datos.

- GET /items/{item_id}: Recupera un registro específico utilizando su ID.

- POST /items: Crea un nuevo registro en la base de datos.

- PUT /items/{item_id}: Actualiza un registro existente identificado por su ID.

- DELETE /items/{item_id}: Elimina un registro de la base de datos utilizando su ID.

#### Integraciones del Proyecto

- Python y FastAPI: El proyecto está desarrollado en Python utilizando el framework FastAPI, que permite construir APIs rápidas y eficientes. Toda la lógica de la API está implementada en el archivo app.py.

- Base de Datos MySQL: El proyecto utiliza MySQL para almacenar los datos de manera persistente. Un script SQL (script.sql) se utiliza para crear las tablas necesarias, y un archivo (querys.sql) se utiliza para agregar datos iniciales.

- HTML: La interfaz de usuario se construye utilizando archivos HTML que se encuentran en el directorio Templates. Estos archivos HTML renderizan la salida de las APIs creadas con FastAPI.

- Biblioteca de Bootstrap: Bootstrap se utiliza para estilizar la interfaz de usuario, haciendo que sea más atractiva y fácil de usar. Los archivos CSS de Bootstrap se encuentran en el directorio Static/Css.

- JavaScript: Se utiliza JavaScript para mejorar la interacción de la página web y asegurar que el documento esté completamente cargado antes de ejecutar cualquier script. Por ejemplo, se puede utilizar el siguiente código para esperar a que el documento esté completamente cargado.

#### Estructura de Carpetas

- Scripts: Contiene el script SQL utilizado para crear la tabla en la base de datos MySQL.

- Static/Css: Contiene los archivos CSS de Bootstrap utilizados para dar estilo a la interfaz de usuario de la aplicación.

- Templates: Aquí se encuentran los archivos HTML que se utilizan para la interfaz de usuario de la aplicación. Estos archivos HTML renderizan la salida de las API creadas con FastAPI.

- Venv: Este directorio contiene el entorno virtual de Python utilizado para aislar las dependencias del proyecto.

- app.py: Este archivo contiene toda la lógica implementada para las API, incluyendo los métodos GET, POST, PUT y DELETE para interactuar con la base de datos y manejar las solicitudes de los clientes.

- requirements.txt contiene una lista de todas las dependencias y versiones de Python necesarias para ejecutar la aplicación. Estas dependencias se instalan automáticamente utilizando la herramienta pip, lo que facilita la configuración del entorno de desarrollo.

<br><img src="https://i.postimg.cc/25d85r4V/estructura.png" alt="">
#### Interfaz de Usuario
Para mejorar la experiencia visual, se ha implementado una página HTML utilizando el framework Bootstrap. Esta página proporciona una interfaz intuitiva para interactuar con las API proporcionadas por la aplicación.

#### Instrucciones para Configurar el Entorno del Proyecto

1.- Clonar el Repositorio:

Clona este repositorio en tu máquina local utilizando el siguiente comando:

	git clone https://github.com/jcarlosmamanidelacruz/Apis-con-fastapi-python.git

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

<br><img src="https://i.postimg.cc/PrkBJ6Zr/python1.png" alt="">

#### Método Get

<br><img src="https://i.postimg.cc/sXC5RZQx/python2-get.png" alt="">

#### Método Post

<br><img src="https://i.postimg.cc/nVyGJz56/python2-post.png" alt="">

#### Método Put

<br><img src="https://i.postimg.cc/766rwXCY/python2-put.png" alt="">

#### Método Delete

<br><img src="https://i.postimg.cc/g0p6SLxK/python2-delete.png" alt="">

#### Captura de Página HTML

<br><img src="https://i.postimg.cc/rm8wBv2d/captura-pagina-html.png" alt="">

#### Captura de un nuevo registro

<br><img src="https://i.postimg.cc/cLqyW7QQ/nuevo-registro.png" alt="">

<br><img src="https://i.postimg.cc/yNc05K7m/lista-registro.png" alt="">

#### Captura de actualización de un registro

<br><img src="https://i.postimg.cc/MK0qShfm/editar-registro.png" alt="">

#### Captura de eliminar un registro

<br><img src="https://i.postimg.cc/Qx2nBQKg/delete-registro.png" alt="">

<br><img src="https://i.postimg.cc/yxzy1PbW/delete-registro-resultado.png" alt="">
