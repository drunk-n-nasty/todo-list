from fastapi import APIRouter, Depends, status, HTTPException
from app.services.category import CategoryNotFound
from app.api.dependencies import get_category_service
from sqlalchemy.orm import Session
from app.schemas.categories import CategoriesSchema, UpdateCategorySchema, CreateCategorySchema

category_route = APIRouter(prefix='/categories')


@category_route.get("")
def read_categories(get_category: Session = Depends(get_category_service)) ->list[CategoriesSchema]:
   return get_category.list_categories()

@category_route.post("", status_code = status.HTTP_201_CREATED)
def create_category(payload: CreateCategorySchema,
                    get_category: Session = Depends(get_category_service)
)-> CategoriesSchema:
    return get_category.create_category(payload)
   

@category_route.patch("/{category_id}")
def update_category(category_id, payload: UpdateCategorySchema, get_category: Session = Depends(get_category_service)):
    try: 
        return get_category.update_category(category_id, payload)
    except CategoryNotFound as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

@category_route.delete("/{category_id}")
def delete_category(category_id, get_category: Session = Depends(get_category_service)):
    try:
        get_category.delete_category(category_id=category_id)
    except CategoryNotFound as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))

