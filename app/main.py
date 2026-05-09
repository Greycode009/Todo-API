from email.mime import text

from fastapi import Depends, FastAPI
from sqlalchemy import text
# from app.config import settings
from app.db.session import get_db
from app.features.todo.route import router as todo_router
from app.features.user.route import router as user
from app.features.todo.service import TodoService
from sqlalchemy.ext.asyncio import AsyncSession


app = FastAPI(title="Todo API", version="1.0.0")

app.include_router(todo_router)
app.include_router(user)

