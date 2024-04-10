
from todos.__db__.table.user import UserTable
from todos.__db__.table.role import RoleTable
from todos.__core__.helper import standard_helper

class AuthenticationService:
    def __init__(self, user_table:UserTable, role_table:RoleTable):
        self.user_db_service = user_table
        self.role_db_service = role_table
        

    
    
    