from sqlalchemy import Column, UUID, ForeignKey

from todos.__db__.schema import Base
from todos.__core__ import constants


class UserCategory(Base):
    
    __tablename__ = constants.TABLE_NAME_MAPPER["USER_CATEGORY"]
    
    id = Column(UUID, primary_key=True)
    user_id = Column(UUID, ForeignKey('user.user_id'))
    category_id = Column(UUID, ForeignKey('category.category_id'))