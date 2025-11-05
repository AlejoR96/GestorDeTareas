# Imagen base de Python
FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /code

# Instalar librerías necesarias para mysqlclient y compilación
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copiar e instalar dependencias de Python
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto al contenedor
COPY . /code/

# Dar permisos al script
RUN chmod +x /code/wait-for-it.sh

# Comando por defecto: ejecutar servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]