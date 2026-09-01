from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db.base import Base
class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key = True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name}, email={self.email})"