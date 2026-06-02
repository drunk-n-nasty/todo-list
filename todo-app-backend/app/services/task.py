from sqlalchemy.orm import Session 
from app.repositories.task import TaskRepository
from app.schemas.tasks import TaskCreateSchema, TaskReadSchema, TaskUpdateSchema

class TaskNotFound(Exception):
    """Задача не найдена по айди"""

class TaskService:
    def __init__(self, db: Session)->None:
        self.db = db 
        self.task_repository = TaskRepository(db)
        
    def list_tasks(self)->list[TaskReadSchema]:
        tasks = self.task_repository.get_all()
        return [TaskReadSchema.model_validate(task) for task in tasks]
        
    def create_task(self, task_create: TaskCreateSchema)->TaskReadSchema:
        task_orm = self.task_repository.create_task(task_create.title)
        self.db.commit()
        return TaskReadSchema.model_validate(task_orm)
    
    def update_task(self, task_id: str, task_update: TaskUpdateSchema)->list[TaskReadSchema]:
        task_orm_for_update = self.task_repository.get_by_id(task_id) 
        if task_orm_for_update is None:
            raise TaskNotFound(f"Задача с {task_id} не найдена.")
        task_orm_for_update.title = task_update.title if task_update.title is not None else task_orm_for_update.title
        task_orm_for_update.completed = task_update.completed if task_update.completed is not None else task_orm_for_update.completed
        self.db.commit()
        return TaskReadSchema.model_validate(task_orm_for_update)
        
    def delete_task(self, task_id:str) -> None:
        task = self.task_repository.get_by_id(task_id)
        if task is None:
            raise TaskNotFound("Задача с {task_id} не найдена.")
        self.task_repository.delete(task)

