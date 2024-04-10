from todos.services.dependancy_injector import Container
from todos.__db__ import connect_db

Services = Container()

RoleService = Services.roleService
UserService = Services.userService
AuthService = Services.authenticationService
