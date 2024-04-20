from dependency_injector import containers, providers
from todos.__db__ import RoleTable, UserTable, UserCategoryTable, CategoryTable

from todos.services.role_management import RoleService
from todos.services.user_management import UserService
from todos.services.category_management import CategoryService

class Container(containers.DeclarativeContainer):
    role_service = providers.Factory(
            RoleService, 
            role_table=RoleTable
        )
    
    user_service = providers.Factory(
            UserService,
            user_table=UserTable,
            user_category_table=UserCategoryTable,
            role_table=RoleTable,
            category_table=CategoryTable
        )
    
    category_service = providers.Factory(
            CategoryService,
            category_table=CategoryTable,
            user_category_table=UserCategoryTable,
            user_table=UserTable
        )
    
    # categoryService = providers.Factory(database.category_table)