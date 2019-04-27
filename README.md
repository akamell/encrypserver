# Encrypserver

## Instalación

1. Clonar el repositorio

```shell
git clone https://github.com/akamell/encrypserver.git
```

2. Instalar paquetes necesarios

```shell
pip install flask flask-cors PyJWT peewee pycryptodome psygcop2 python-dotenv
```

3. Crear archivo .env en la carpeta raiz del repositorio

```shell
touch .env
```

Copia lo siguiente texto en el archivo (.env), reemplazando respectivamente por la configuración de tu base de datos de PostgresSQL

```
DB_NAME = <nombre de la base datos>
DB_HOST = <host del servidor>
DB_PORT = <puerto>
DB_USER = <usuario>
DB_PASS = <contraseña>
DB_SCHEMA = <schema>
```

4. Correr en el directorio del repositorio

```shell
py run.py
```
