from celery import Celery
# from fastapi import BackgroundTasks
from decouple import config

celery_app = Celery(
    "tasks",
    broker=config('RABBIT_URL')
)

@celery_app.task()
def hello_wolrd():
    return 'hi dear'


@celery_app.task
def send_email(user_email, subject, message):
    # background_tasks.add_task(write_notification,email= subject, message=message)
    celery_app.send_task("send_email")
    # Lógica para enviar e-mails
    # Substitua isso pela lógica real de envio de e-mails
    print(f"Sending email to {user_email} with subject: {subject}, and message: {message}")