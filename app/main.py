from email.mime import text

from fastapi import Depends, FastAPI
from sqlalchemy import text
# from app.config import settings
from app.db.session import get_db
from app.features.todo.route import router as todo_router
from app.features.todo.service import TodoService
from sqlalchemy.ext.asyncio import AsyncSession


app = FastAPI(title="Todo API", version="1.0.0")

# app.include_router(todo_router)

@app.get("/")
async def root(db: AsyncSession = Depends(get_db)):
    # print(settings.DATABASE_URL)
    print("Testing database connection...")
    result = await db.execute(text("SELECT 1"))
    print("Database connection successful!")
    return {"message": "Connected to the database", "result": result.scalar()}
