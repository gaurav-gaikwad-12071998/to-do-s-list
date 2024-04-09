from sqlalchemy.orm import declarative_base

Base = declarative_base()

from todos.__db__.schema.role import Role 
from todos.__db__.schema.user import User 
from todos.__db__.schema.category import Category 
from todos.__db__.schema.user_category import UserCategory 
from todos.__db__.schema.task import Task 


async def create_all_tables(engine):
        """
        A function to create all tables in the database asynchronously.
        """
        try:
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            print("All tables created successfully.")
        except Exception as e:
            print(e)