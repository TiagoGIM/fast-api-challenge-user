FROM python:3.10.4-slim-buster
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --upgrade -r /code/requirements.txt
COPY ./celery_tasks.py /code/
CMD ["celery", "-A", "celery_tasks.celery_app", "worker", "--loglevel=INFO"]