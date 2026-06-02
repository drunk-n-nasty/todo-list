from app.models.category import CategoryORM
from sqlalchemy.orm import Session
from sqlalchemy import select


class CategoryRepository:
    def __init__(self, db: Session)-> None:
        self.db = db 

    def read_categories(self)->list[CategoryORM]:
        categories = self.db.scalars(select(CategoryORM)).all()        
        return categories 

    def get_by_id(self, category_id:str)->CategoryORM:
        obj = self.db.get(CategoryORM, category_id)
        return obj
    
    def create_category(self, name) -> CategoryORM:
        new_category = CategoryORM(name = name)
        self.db.add(new_category)
        return new_category

    def delete_category(self, obj: CategoryORM) -> None:
        self.db.delete(obj )
        self.db.commit()

    
