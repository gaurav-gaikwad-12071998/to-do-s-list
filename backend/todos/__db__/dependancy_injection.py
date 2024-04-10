from dependency_injector import containers, providers


from todos.__db__.database import DatabaseService

from todos.__db__.schema import Category, Role, Task, User, UserCategory
from todos.__db__.table.category import CategoryTable
from todos.__db__.table.role import RoleTable
from todos.__db__.table.task import TaskTable
from todos.__db__.table.user_category import UserCategoryTable
from todos.__db__.table.user import UserTable


class Container(containers.DeclarativeContainer): 
    # Define providers for DatabaseService
    database_service = providers.Singleton(DatabaseService)
    
    # Define providers for Category and CategoryTable
    category = providers.Singleton(Category)
    category_table = providers.Factory(CategoryTable, table_class=Category)

    # Define providers for Role and RoleTable
    role = providers.Singleton(Role)
    role_table = providers.Factory(RoleTable, table_class=Role)
    
    # Define providers for Task and TaskTable
    task = providers.Singleton(Task)
    task_table = providers.Factory(TaskTable, table_class=Task)
    
    # Define providers for UserCategory and UserCategoryTable
    user_category = providers.Singleton(UserCategory)
    user_category_table = providers.Factory(UserCategoryTable, table_class=UserCategory)
    
    # Define providers for User and UserTable
    user = providers.Singleton(User)
    user_table = providers.Factory(UserTable, table_class=User)
