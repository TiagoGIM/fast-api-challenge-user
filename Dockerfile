# Define a imagem base utilizando o Python 3.11.4 com uma distribuição Linux mínima (Slim Buster)
FROM python:3.10.4-slim-buster

# Define o diretório de trabalho como /code
WORKDIR /code

# Copia o arquivo requirements.txt para o diretório /code
COPY ./requirements.txt /code/requirements.txt

COPY ./alembic.ini /code/alembic.ini

# Atualiza o sistema e instala as dependências necessárias, incluindo o libpq-dev e gcc
RUN apt-get update && apt-get -y install libpq-dev gcc

# Instala as dependências do projeto, utilizando o pip e o arquivo requirements.txt
RUN pip install --upgrade -r /code/requirements.txt

# Copia o diretório app para o diretório /code/app
COPY ./app /code/app
COPY ./run_alembic.sh /code/run_alembic.sh

RUN chmod +x /code/run_alembic.sh

# RUN python /code/app/seeds/create_admin_user.py

# Comando que será executado ao iniciar o contêiner, iniciando o servidor Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]