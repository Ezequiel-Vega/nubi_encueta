# Flask Encuestas
apiREST creada con Python y FLask para realizar encuestas en una aplicacion web.

# Quickstart
Se pude iniciar de dos maneras diferentes el apiREST, la primera es desde el codigo fuente y la segunda es usando Docker.

## desde el codigo fuente
se tendra que crear un fichero ``.env`` en donde se tendra que declarar las siguientes variables
- ``HOST`` _para declarar el host de la api_
- ``PORT`` _para declarar el puerto/port de la api_
- ``DEBUG`` _para indicar si esta en modo debug, declarar **1** si es verdadero y **0**  si es falso_
- ``SECRET_KEY`` _para declarar la llave secreta de la api_
- ``JWT_SECRET_KEY`` _para declarar la llave secreta del token_
- ``DATABASE_URI`` _para colocar la url de la base de datos ejemplo: postgresql://user:password@host:port/namedatabase_

Ya que se declaro las variables de entrono se tiene que instalar las dependencias del proyecto, para ello se crea un entorno virtual con el comando ``python -m venv env`` e inicializamos el mismo con el comando(esto depende del sistema operativo que utilizas)

- **Unix:** ``. env/bin/active``
- **Windows:** ``env/Script/active.bat``

Ya que tenemos el entorno virtual iniciado instalaremos las dependencias del proyecto con el comando:
``pip install -r requirements.txt``

Una vez creado el entorno virtual e instalado las dependencias, se tiene que inicar el archivo **entrypoint.py** con el siguiente comando ``python entrypoint.py``. Listo ya tenemos nuestra apiREST funcionando.

## Usando Docker
Para inicar el apiREST desde Docker solamente se tiene que ejecutar los siguientes comandos desde la carpeta del proyecto: 

``docker build -t app .``

``docker run -d
    --name app 
    -e HOST=host 
    -e PORT=port 
    -e DEBUG=debug 
    -e SECRET_KEY=secretkey 
    -e JWT_SECRET_KEY=jwtsecretkey 
    -e DATABASE_URI=postgresql://user:password@host:port/namedatabase 
    app
    ``