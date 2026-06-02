from sqlalchemy.orm import Session
from app.models.task import TaskORM
from sqlalchemy import select

class TaskRepository:
    def __init__(self, db: Session) -> None:
        self.db = db 


    def get_all(self)-> list[TaskORM]:
        return self.db.scalars(select(TaskORM)).all()
    
    def get_by_id(self, task_id: str)-> TaskORM | None :
        obj = self.db.get(TaskORM, task_id)
        return obj
    
    def create_task(self, title:str ) -> TaskORM:
        obj = TaskORM(title=title, completed = False)
        self.db.add(obj)
        return obj

    def delete(self, obj: TaskORM) -> None:
       self.db.delete(obj)
       self.db.commit()
