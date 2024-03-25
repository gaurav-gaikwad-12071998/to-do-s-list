
from todos.__db__.schema import Base
from sqlalchemy import Column, UUID, VARCHAR, BOOLEAN


class Category(Base):
    __tablename__ = "category"
    
    category_id = Column(UUID, primary_key=True)
    category_title = Column(VARCHAR(50))
    is_default = Column(BOOLEAN)