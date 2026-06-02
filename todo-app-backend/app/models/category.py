from .base import Base 
from sqlalchemy.orm import Mapped, mapped_column


class CategoryORM(Base):
    __tablename__ = 'categories'
    name: Mapped[str]
