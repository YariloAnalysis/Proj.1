from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from db.base import Base

PG_URL = "postgresql+asyncpg://admin:1234@localhost:5432/testdb"

async def init_postgres():
    engine = create_async_engine(PG_URL, echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False)
    return sessionmaker, engine