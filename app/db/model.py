

from sqlalchemy import Boolean, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


# Define the User model
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    username: Mapped[str] = mapped_column(
        String,
        unique=True
    )

    email: Mapped[str] = mapped_column(
        String,
        unique=True
    )

    # Relationship
    todos = relationship(
        "Todo",
        back_populates="user",
        cascade="all, delete"
    )


# Define the Todo model

class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)


 # Foreign Key
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    # Relationship
    user = relationship(
        "User",
        back_populates="todos"
    )