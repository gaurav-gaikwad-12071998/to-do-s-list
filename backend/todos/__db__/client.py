import os
import dotenv

from sqlalchemy import  Column, Integer, String, text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from todos.__db__.schema import create_all_tables

dotenv.load_dotenv()

USER_NAME = os.getenv("USER_NAME")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DATABASE = os.getenv("DATABASE")

async def create_db():
    db_name = DATABASE
    # db_url = "postgresql://{USER_NAME}:{PASSWORD}@{HOST}:{PORT}/postgres"
    engine = create_async_engine(f"postgresql+asyncpg://{USER_NAME}:{PASSWORD}@{HOST}:{PORT}/postgres", isolation_level="AUTOCOMMIT")
    # engine = create_engine(db_url)
    try:
        
        async with engine.connect() as conn:
            await conn.execute(text(f"CREATE DATABASE {db_name}"))
        print(f"Database '{db_name}' created successfully")
    except Exception as e:
        if 'already exists' in str(e):
            print(f"Database '{db_name}' already exists")
        else:
            # If any other error occurs, print the error
            print("An error occurred:", e)
    finally:
        await engine.dispose()

# Database connection details (replace with your actual credentials)
DATABASE_URL = f"postgresql+asyncpg://{USER_NAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"


engine = create_async_engine(DATABASE_URL)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False, autocommit=False, autoflush=False)

async def create_all_tables_async():
    return await create_all_tables(engine)



# Define a base class for your ORM models

    
# async def get_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         print("db close")
#         await db.close()
        
# async def get_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)
#     db = SessionLocal()
#     return db
   

# async def create_user(db: AsyncSession, name: str, email: str):
#     """
#     Creates a new user record in the database.
#     """

 
#     new_user = User(name=name, email=email)
#     db.add(new_user)
#     await db.commit()
#     # await db.refresh(new_user)  # Refresh to get generated ID
#     return new_user

# async def main():
#     """
#     Example usage of the asynchronous functions.
#     """

#     async with await get_db() as session:
#         user = await create_user(session, "Alice", "alice13@example.com")
#         print(f"Created user:  {user.name} ({user.email})")
  
    
# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(main())
#     # engine = create_async_engine(DATABASE_URL)
    
#     # async_sessionmaker(engine)
    
  
    

    
    
    
