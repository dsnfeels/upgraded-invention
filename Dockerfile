# Usa a imagem oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . .

# Define o comando que será executado ao rodar o container
CMD ["python", "main.py"]
