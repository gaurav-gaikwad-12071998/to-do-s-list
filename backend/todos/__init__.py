from todos.services.dependancy_injector import Container
from todos.__db__ import connect_db
from todos.__core__.constants import MESSAGES

Services = Container()

RoleService = Services.role_service
UserService = Services.user_service
CategoryService = Services.category_service

