
from todos.__db__.schema import Base
from sqlalchemy import Column, UUID, VARCHAR, DATE, BOOLEAN, TIMESTAMP, ForeignKey, func





class User(Base):
    __tablename__ = "user"

    user_id = Column(UUID, primary_key=True)
    user_name = Column(VARCHAR(300), nullable=False)
    user_contact = Column(VARCHAR(20), nullable=False)
    user_email = Column(VARCHAR(100), unique=True, nullable=False)
    user_birthdate = Column(DATE)
    role_id = Column(UUID, ForeignKey('role.role_id'), nullable=False)
    verified = Column(BOOLEAN, default=False)
    password = Column(VARCHAR(300), nullable=False)
    created_at = Column(TIMESTAMP, default=func.now())
    updated_at = Column(TIMESTAMP, default=func.now(), onupdate=func.now())
    
    
    
    
      
        