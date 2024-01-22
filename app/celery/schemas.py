from pydantic import BaseModel

class TaskModel(BaseModel):
    task_id: str
    task_status: str

class TaskResultModel(BaseModel):
    task_id: str
    task_status: str
    payload: str