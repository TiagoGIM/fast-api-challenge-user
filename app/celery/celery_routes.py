from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from .celery_tasks import hello_wolrd
router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

# async def trigger_send_email(user_email: str, subject: str, message: str):
#     try:
#         send_email.delay(user_email, subject, message)
#         return {"message": "E-mail scheduled for sending."}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Failed to send e-mail: {str(e)}")

@router.get('/hello-world')
async def task_hellow_wolrd():
    try: 
        hello_wolrd.delay()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to hello wolrd: {str(e)}")

