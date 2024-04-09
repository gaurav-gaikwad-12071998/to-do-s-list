# from sqlalchemy import  Column, Integer, String
# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
# from sqlalchemy.orm import declarative_base

# # Database connection details (replace with your actual credentials)
# DATABASE_URL = "postgresql+asyncpg://postgres:admin@localhost:5432/database_test"


# engine = create_async_engine(DATABASE_URL)
# SessionLocal = async_sessionmaker(engine, expire_on_commit=False, autocommit=False, autoflush=False)



# # Define a base class for your ORM models
# Base = declarative_base()

# # Define a simple User model
# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True)
#     name = Column(String)

    
# # async def get_db():
# #     async with engine.begin() as conn:
# #         await conn.run_sync(Base.metadata.create_all)
# #     db = SessionLocal()
# #     try:
# #         yield db
# #     finally:
# #         print("db close")
# #         await db.close()
        
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
    

from todos import RoleTable, UserTable, connect_db
from todos.__db__.types.table_user import userInsertParams
from todos.__db__.types.table_role import roleInsertParams
from sqlalchemy import UUID
from uuid import uuid4
from datetime import date

async def main():
    
    # role_table = RoleTable()
    
    # role_params:roleInsertParams = {
    #     "role_id" : uuid4(),
    #     "role_title" : "editor",
    #     "role_description" : "Editor has only features access"
    # }
    
    # await role_table.insert(role_params)
    
    user_table = UserTable()

    # await user_table.create_all_tables()
    
    # user_params: userInsertParams = {
    #     "user_id" : uuid4(),
    #     "user_name" : "Naruto Uzumaki",
    #     "password" : "Hinata@123",
    #     "role_id" : "20e4f8bf-a8b9-4717-9ba2-3d93fb0fd18e",
    #     "user_birthdate" : date(1998, 10, 10),
    #     "user_contact" : "9988776655",
    #     "user_email" : "naruto7@anime.com",
    #     "verified" : False
    # }
     
    # result = await user_table.update_by_id('91619ebf-13aa-4e2c-8208-d6faf2d1204b', {"user_name" : "Sasuke Uchiha"})
    result = await user_table.delete_by_id('91619ebf-13aa-4e2c-8208-d6faf2d1204b')
    print(result)
    
import asyncio    
    
if __name__ == "__main__":
    asyncio.run(connect_db())
    # import asyncio
    # asyncio.run(main())

# import bcrypt
# # salt = bcrypt.gensalt()
# salt = b'$2b$12$SeBUnjglzcwubwx6LE30O.'

# password = "Hinata@123"



# hashed = bcrypt.hashpw(bytes(password, encoding="utf-8"), salt)
    
  
# print("Salt :")
# print(salt)

# print("Hashed")
# print(hashed)

# import os

# def generate_fixed_salt():
#   """
#   Generates a cryptographically secure random byte string for fixed salt.
#   """
#   return os.urandom(32)

# from todos.__core__ import constants
# from argon2 import PasswordHasher

# fixed_salt = constants.DB_SALT
# print(fixed_salt)

# ph = PasswordHasher()

# # Hashing a password
# password = "your_password"
# hashed_password = ph.hash(password.encode(), salt=fixed_salt)
# print(f"Hashed password: {hashed_password}")

# # Verifying a password
# user_input_password = "your_password"  # Replace with user input
# try:
#   ph.verify(hashed_password, user_input_password)
#   print("Password is correct")
# except:
#   print("Password is incorrect")