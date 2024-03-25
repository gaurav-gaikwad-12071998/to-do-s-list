from sqlalchemy import  Column, Integer, String
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


# Database connection details (replace with your actual credentials)
DATABASE_URL = "postgresql+asyncpg://postgres:admin@localhost:5432/database_test"


engine = create_async_engine(DATABASE_URL)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False, autocommit=False, autoflush=False)



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
    
  
    

    
    
    
