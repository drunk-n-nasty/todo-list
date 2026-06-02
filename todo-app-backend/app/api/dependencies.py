from sqlalchemy.orm import Session
from fastapi import Depends
from app.db.sessions import get_gb
from app.services.task import TaskService
from app.services.category import CategoryService


def get_task_service(db: Session = Depends(get_gb)):
    return TaskService(db)

def get_category_service(db: Session = Depends(get_gb)):
    return CategoryService(db)