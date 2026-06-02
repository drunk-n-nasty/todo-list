from fastapi import APIRouter, status, Depends, HTTPException
from app.schemas.tasks import TaskCreateSchema, TaskReadSchema, TaskUpdateSchema
from app.services.task import TaskService
from app.api.dependencies import get_task_service
from sqlalchemy.orm import Session 
from app.services.task import TaskNotFound


task_router = APIRouter(prefix='/tasks')

@task_router.get("")
def read_task(task_service: Session = Depends(get_task_service))-> list[TaskReadSchema]:
    return task_service.list_tasks()

@task_router.post("", status_code = status.HTTP_201_CREATED)
def create_task(payload: TaskCreateSchema,
                task_service: Session = Depends(get_task_service)
)-> TaskReadSchema:
    return task_service.create_task(task_create=payload)

@task_router.patch("/{task_id}")
def update_taks(task_id: str,
                payload: TaskUpdateSchema,
                task_service: Session = Depends(get_task_service)
)-> TaskReadSchema:
    try: 
        return task_service.update_task(task_id=task_id, task_update=payload)
    except TaskNotFound as e:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = str(e))

@task_router.delete("/{task_id}")
def delete_task(task_id: str, task_service: Session = Depends(get_task_service)):
    try:
        return task_service.delete_task(task_id)
    except TaskNotFound as e:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = str(e))

