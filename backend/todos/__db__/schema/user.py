
from todos.__db__.schema import Base
from sqlalchemy import Column, UUID, VARCHAR, DATE, BOOLEAN, TIMESTAMP, ForeignKey, func
from todos.__core__ import constants
from argon2 import PasswordHasher




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
    
    password_hasher = PasswordHasher()
    
    async def hash_password(self):
        self.password =  self.password_hasher.hash(self.password.encode(), salt=constants.DB_SALT)
        
    async def verify_password(self, hashed_password, user_input_password):
        try:
          self.password_hasher.verify(hashed_password, user_input_password)
          return True
        except:
          return False
      
        