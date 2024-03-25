from sqlalchemy.orm import declarative_base

Base = declarative_base()

from todos.__db__.schema.role import Role 
from todos.__db__.schema.user import User 
from todos.__db__.schema.category import Category 
from todos.__db__.schema.user_category import UserCategory 
from todos.__db__.schema.task import Task 