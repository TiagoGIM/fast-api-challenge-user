from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from .celery_tasks import send_email
router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

@router.get('/test-task')
async def task_hellow_wolrd():
    try: 
        task = send_email.delay('email@test')
        return task.id
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to Creat Task send-email : {str(e)}")

