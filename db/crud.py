from sqlalchemy import select
from db.models import User
from sqlalchemy.ext.asyncio import AsyncSession

async def create_user(session: AsyncSession, name: str,email: str) -> User:
    user = User(name=name, email=email)
    session.add(user)
    await session.commit()
    await session.refresh(user)
    return user
async def get_user_by_email(session: AsyncSession, email: str) -> User | None:
    """Получает пользователя по email."""
    result = await session.execute(select(User).where(User.email == email))
    return result.scalar_one_or_none()


async def list_users(session: AsyncSession) -> list[User]:
    """Возвращает список всех пользователей."""
    result = await session.execute(select(User))
    return result.scalars().all()


async def delete_user(session: AsyncSession, user_id: int) -> bool:
    """Удаляет пользователя по ID."""
    user = await session.get(User, user_id)
    if user:
        await session.delete(user)
        await session.commit()
        return True
    return False