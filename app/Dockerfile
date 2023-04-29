FROM python:3

# espaço de trabalho 
WORKDIR /usr/src
COPY . /usr/src/app/

# Variaveis de anbiente
ENV DOCKERENV=True
ENV FLASK_ENV=development
ENV FLASK_APP __init__.py
ENV FLASK_RUN_HOST 0.0.0.0

RUN apt update -y
RUN pip install --upgrade pip
RUN pip install psycopg2
RUN pip install -r app/requirements.txt

CMD [ "sh", "app/entrypoint.sh" ]
