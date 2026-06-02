from sqlalchemy.orm import Session
from app.repositories.category import CategoryRepository
from app.schemas.categories import CategoriesSchema, CreateCategorySchema, UpdateCategorySchema

class CategoryNotFound(Exception):
    """Категория не найдена"""

class CategoryService:

    def __init__(self, db: Session)->None:
        self.db = db 
        self.category_repository = CategoryRepository(db)
    
    def list_categories(self) -> list[CategoriesSchema]:
        categories = self.category_repository.read_categories() 
        return [CategoriesSchema.model_validate(cat) for cat in categories]
    
    def create_category(self, payload: CreateCategorySchema)->CategoriesSchema:
        new_category = self.category_repository.create_category(payload.name)
        self.db.commit()
        return CategoriesSchema.model_validate(new_category)
    
    def update_category(self, category_id: str, payload: UpdateCategorySchema) -> CategoriesSchema:
        category_for_update = self.category_repository.get_by_id(category_id=category_id)
        if category_for_update is None:
            raise CategoryNotFound(f'Категория c id - {category_id} не найдена.')
        category_for_update.name = payload.name if payload.name is not None else category_for_update.name 
        self.db.commit()
        return CategoriesSchema.model_validate(category_for_update)

    def delete_category(self, category_id:str) -> None:
        category_for_delete = self.category_repository.get_by_id(category_id=category_id)
        if category_for_delete is None:
            raise CategoryNotFound(f'Категория c id - {category_id} не найдена.')
            
        self.category_repository.delete_category(category_for_delete)
