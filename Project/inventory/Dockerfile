FROM python:3.13.7-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivo de dependencias primero (para aprovechar la cache de Docker)
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código de la aplicación
COPY . .

# Exponer el puerto en el que correrá FastAPI
EXPOSE 8000

# Comando para arrancar el servidor con uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
