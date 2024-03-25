from sqlalchemy.orm import declarative_base, declared_attr
from sqlalchemy import  Column, UUID, VARCHAR, DATE, NUMERIC, BOOLEAN, TIMESTAMP, ForeignKey, TEXT, func
from datetime import date


Base = declarative_base()

class Role(Base):
    __tablename__ = "role"
    
    role_id = Column(UUID, primary_key=True)
    role_title = Column(VARCHAR(10))
    role_description = Column(VARCHAR(50))


class User(Base):
    __tablename__ = "user"

    user_id = Column(UUID, primary_key=True)
    user_name = Column(VARCHAR(300))
    user_contact = Column(VARCHAR(20))
    user_email = Column(VARCHAR(100), unique=True)
    user_birthdate = Column(DATE)
    
    role_id = Column(UUID, ForeignKey('role.role_id'))
    verified = Column(BOOLEAN)
    password = Column(VARCHAR(300))
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())
    
    @declared_attr
    def user_age(cls):
        """Calculates the age based on the birthdate."""

        def calculate_age(self):
            if self.birthdate:
                today = date.today()
                return today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
            else:
                return None

        return Column(NUMERIC, nullable=True, onupdate=calculate_age)
    

class Category(Base):
    __tablename__ = "category"
    
    category_id = Column(UUID, primary_key=True)
    category_title = Column(VARCHAR(50))
    is_default = Column(BOOLEAN)

    
class Task(Base):
    __tablename__ = "task"
    
    task_id = Column(UUID, primary_key=True)
    task_title = Column(VARCHAR(100))
    task_description = Column(TEXT)
    category_id = Column(UUID, ForeignKey('category.category_id'))
    task_due = Column(TIMESTAMP)
    task_status = Column(VARCHAR(15))
    task_priority = Column(VARCHAR(10))
    user_id = Column(UUID, ForeignKey('user.user_id'))
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())
    
    
class User_Category(Base):
    __tablename__ = 'user_category'
    user_id = Column(UUID)
    category_id = Column(UUID)
    
