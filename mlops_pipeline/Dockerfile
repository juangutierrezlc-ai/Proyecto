# Imagen base
FROM python:3.10

# Crear directorio de trabajo
WORKDIR /app

# Copiar archivos
COPY . /app

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer puerto
EXPOSE 8000

# Comando de arranque
CMD ["uvicorn", "model_deploy:app", "--host", "0.0.0.0", "--port", "8000"]

