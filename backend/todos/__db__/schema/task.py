from sqlalchemy import Column, UUID, VARCHAR, TEXT, TIMESTAMP, ForeignKey, func

from todos.__db__.schema import Base
from todos.__core__ import constants

class Task(Base):
    __tablename__ = constants.TABLE_NAME_MAPPER["TASK"]
    
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

