from todos.__db__.schema import Base
from sqlalchemy import Column, UUID, ForeignKey


class UserCategory(Base):
    __tablename__ = 'user_category'
    id = Column(UUID, primary_key=True)
    user_id = Column(UUID, ForeignKey('user.user_id'))
    category_id = Column(UUID, ForeignKey('category.category_id'))