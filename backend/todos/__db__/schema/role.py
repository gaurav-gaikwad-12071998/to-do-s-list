from sqlalchemy import Column, UUID, VARCHAR

from todos.__db__.schema import Base
from todos.__core__ import constants

class Role(Base):
    __tablename__ = constants.TABLE_NAME_MAPPER["ROLE"]
    
    role_id = Column(UUID, primary_key=True)
    role_title = Column(VARCHAR(10), unique=True)
    role_description = Column(VARCHAR(50))
    
