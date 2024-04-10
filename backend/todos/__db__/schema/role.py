
from todos.__db__.schema import Base
from sqlalchemy import Column, UUID, VARCHAR


class Role(Base):
    __tablename__ = "role"
    
    role_id = Column(UUID, primary_key=True)
    role_title = Column(VARCHAR(10), unique=True)
    role_description = Column(VARCHAR(50))
    
