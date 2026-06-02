from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.api.routers.task import task_router
from app.api.routers.category import category_route

from app.models.base import Base
from .db.sessions import engine
from app.core.config import get_settings

settings = get_settings()

@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind = engine)
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(router=task_router)
app.include_router(router=category_route)


app.add_middleware(
    CORSMiddleware,
    allow_origins = settings.allow_origins,
    allow_methods = ["*"],
)

