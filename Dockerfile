# Imagen base
FROM python:3.10.4-slim-bullseye

# Seteo de variables de entorno
# Deshabilita el chequeo de versiones en pip
ENV PIP_DISABLE_PIP_VERSION_CHECK 1 
# Evita que se generen archivos .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# La salida estandard de Python se muestra de forma inmediata
ENV PYTHONUNBUFFERED 1 

# Seteo del directorio de trabajo
WORKDIR /code

# Intalar dependencias
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copia el proyecto
COPY . .
