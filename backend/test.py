from sqlalchemy import Column, VARCHAR, BOOLEAN
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from dependency_injector import containers, providers

Base = declarative_base()

class Category(Base):
    __tablename__ = "category"
    
    category_id = Column(UUID, primary_key=True)
    category_title = Column(VARCHAR(50))
    is_default = Column(BOOLEAN)


class DatabaseService:
    def __init__(self, table_class):
        self.table_class = table_class


class CategoryTable(DatabaseService):
    def __init__(self, table_class: Category):
        super().__init__(table_class)
        self.primary_key = "category_id"


class CategoryService:
    def __init__(self, category_table: CategoryTable):
        self.db_service = category_table

# class DependencyContainer(containers.DeclarativeContainer):
#     # Define providers for Category, DatabaseService, CategoryTable, and CategoryService
#     category_provider = providers.Singleton(Category)
#     database_service_provider = providers.Singleton(DatabaseService)
#     category_table_provider = providers.Factory(CategoryTable, table_class=category_provider)
#     category_service_provider = providers.Factory(CategoryService, category_table=category_table_provider)

# Now you can use category_service_instance which would have the dependencies injected


class DatabaseDependencyContainer(containers.DeclarativeContainer):
    # Define providers for Category, DatabaseService, CategoryTable, and CategoryService
    category_provider = providers.Singleton(Category)
    database_service_provider = providers.Singleton(DatabaseService)
    category_table_provider = providers.Factory(CategoryTable, table_class=category_provider)

databaseDependencyContainer = DatabaseDependencyContainer()
class ServiceDependencyContainer(containers.DeclarativeContainer):
    category_service_provider = providers.Factory(CategoryService, category_table=databaseDependencyContainer.category_table_provider)



    

    


from todos import UserService
import asyncio
import datetime

userService = UserService()

        



if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    # tasks = [
    #     userService.create_user("Naruto Uzumaki", "nU9aP@example.com", "123456", "123456", "1234567890", datetime.datetime.strptime('2024-04-09', '%Y-%m-%d'), 'admin') 
    #     for _ in range(1)
    # ]
    # loop.run_until_complete(asyncio.gather(*tasks))
    data = asyncio.run(userService.get_user_by_email("nU9aP@.com"))
    print(data)