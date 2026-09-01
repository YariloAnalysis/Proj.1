from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from db.base import Base

MYSQL_URL = "mysql+aiomysql://root:1234@localhost:3306/testdb"

async def init_mysql():
    engine = create_async_engine(MYSQL_URL, echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    sessionmaker = async_sessionmaker(engine, expire_on_commit=False)
    return sessionmaker, engine