
from sqlalchemy import Column, UUID, VARCHAR, DATE, BOOLEAN, TIMESTAMP, ForeignKey, func

from todos.__db__.schema import Base
from todos.__core__ import constants



class User(Base):
    __tablename__ = constants.TABLE_NAME_MAPPER["USER"]

    user_id = Column(UUID, primary_key=True)
    user_name = Column(VARCHAR(300), nullable=False)
    user_contact = Column(VARCHAR(20), nullable=False)
    verified_contact = Column(BOOLEAN, default=False)
    user_email = Column(VARCHAR(100), unique=True, nullable=False)
    verified_email = Column(BOOLEAN, default=False)
    user_birthdate = Column(DATE)
    role_id = Column(UUID, ForeignKey('role.role_id'), nullable=False)
    password = Column(VARCHAR(300), nullable=False)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())
    
    
    
    
      
        