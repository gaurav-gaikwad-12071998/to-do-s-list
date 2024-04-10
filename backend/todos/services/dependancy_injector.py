from dependency_injector import containers, providers
from todos.__db__ import RoleTable, UserTable, UserCategoryTable

from todos.services.role_management import RoleService
from todos.services.user_management import UserService
from todos.services.authentication_management import AuthenticationService

class Container(containers.DeclarativeContainer): 
    roleService = providers.Factory(RoleService, role_table=RoleTable)
    userService = providers.Factory(UserService, user_table=UserTable, user_category_table=UserCategoryTable, role_table=RoleTable)
    authenticationService = providers.Factory(AuthenticationService, user_table=UserTable, role_table=RoleTable)
    # categoryService = providers.Factory(database.category_table)
    # categoryService = providers.Factory(database.category_table)