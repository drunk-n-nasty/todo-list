from pydantic import BaseModel, ConfigDict

class CategoriesSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: str 
    name: str

class CreateCategorySchema(BaseModel):
    name: str

class UpdateCategorySchema(BaseModel):
    name: str | None = None