from pydantic import BaseModel

class TaskModel(BaseModel):
    task_id: str
    task_status: str

class TaskResultModel(BaseModel):
    task_id: str
    task_status: str
    payload: str


#   celery:
#     build:
#       context: ./app/celery
#       dockerfile: celery_worker.dockerfile
#     restart: always
#     depends_on:
#       - rabbitmq
#     networks:
#       - network-api

#   flower:
#     image: mher/flower:1.2
#     environment:
#       - CELERY_BROKER_URL=${RABBIT_URL}
#     restart: always
#     ports:
#       - 5555:5555
#     depends_on:
#       - celery
# networks:
#   network-api:
#     driver: bridge