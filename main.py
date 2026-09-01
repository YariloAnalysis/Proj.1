import asyncio
from db.mysql import init_mysql
from db.postgres import init_postgres
from db.crud import create_user, list_users

async def main():
    mysql_sessionmaker, mysql_engine = await init_mysql()
    pg_sessionmaker, pg_engine = await init_postgres()
    async with mysql_sessionmaker() as session:
        await create_user(session,"MySQL User", "mysql@example.com")
        users = await list_users(session)
        print('[MySQL users]',users)
    async with pg_sessionmaker() as session:
        await create_user(session, "Postgres User", "pg@example.com")
        users = await list_users(session)
        print("[Postgres users]", users)
    await mysql_engine.dispose()
    await pg_engine.dispose()
if __name__ == '__main__':
    asyncio.run(main())
