from celery import Celery
# from fastapi import BackgroundTasks
from decouple import config
from celery.utils.log import get_task_logger

celery_log = get_task_logger(__name__)

celery_app = Celery(
    "tasks",
    broker=config('RABBIT_URL'),
)

@celery_app.task()
def hello_wolrd():
    return 'hi dear'


@celery_app.task(
        name="send_email",
        bind="true",
        retry_backoff=True,
        autoretry_for=(ValueError,)
)
def send_email(self,user_email):
    celery_log.info("Email has been sent")
    message = f"Email has been sent to {user_email}"
    #TODO: implement service to send email
    print(f"Sending email to {user_email} and message: {message}")
    return {
        "msg": message,
        "details": {
            "destination": user_email,
        },
    }