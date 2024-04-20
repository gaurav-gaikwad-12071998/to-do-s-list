from sqlalchemy import Column, UUID, VARCHAR, BOOLEAN

from todos.__db__.schema import Base
from todos.__core__ import constants

class Category(Base):
    __tablename__ = constants.TABLE_NAME_MAPPER["CATEGORY"]
    
    category_id = Column(UUID, primary_key=True)
    category_title = Column(VARCHAR(50))
    is_default = Column(BOOLEAN)