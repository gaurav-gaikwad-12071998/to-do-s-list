import uuid
import datetime
from argon2 import PasswordHasher

from todos.__db__.table.user import UserTable
from todos.__db__.table.user_category import UserCategoryTable
from todos.__db__.table.role import RoleTable
from todos.__core__ import constants
from todos.__core__.helper import standard_helper



class UserService:
    def __init__(
            self, 
            user_table: UserTable, 
            user_category_table: UserCategoryTable, 
            role_table: RoleTable
        ):
        self.user_db_service = user_table
        self.user_category_db_service = user_category_table
        self.role_db_service = role_table
        self.roles = None
    
    
        
    async def create_user(self, user_name:str, user_email:str, user_password:str, confirm_password:str, user_contact:str, user_birthdate:str, role:str):
        try:
            # check if password and confirm password is same
            if(user_password != confirm_password):
                raise Exception("Password and confirm password should be same.")
                        
            # created params to insert user
            params = {
                self.user_db_service.primary_key : str(uuid.uuid4()),
                "user_name": user_name,
                "user_email": user_email,
                "password": standard_helper.hash_password(user_password),
                "user_contact" : user_contact,
                "user_birthdate": user_birthdate,
                "role_id" : await self.get_role_id_by_title(role) # to get role id
            }
            await self.user_db_service.insert(params)
            
            print("User created successfully.")
            
        except Exception as e:
            
            # print(e.args[0])
            raise e
        
    async def get_role_id_by_title(self, role_title:str):
        try:
            if(self.roles == None):
                self.roles =await self.role_db_service.get_all()
            role_data = list(filter( lambda x: x["role_title"] == role_title.upper(), self.roles))[0]
            return role_data["role_id"]
        except Exception as e:
            raise e
        
    async def get_all_users(self):
        all_user = await self.user_db_service.get_all()
        for item in all_user:
            del item["password"]
        return all_user
    
    async def get_user_by_email(self, email:str):
        try:
            result = await self.user_db_service.get_by_query({"user_email":email})
            return result[0]
        except Exception as e:
            raise e
        
    async def login_user(self, email:str, password:str):
        try:
            user_data = await self.get_user_by_email(email)
            if(user_data == None):
                raise Exception("User not found.")
            
            if(standard_helper.verify_password(user_data["password"], password) == False):
                raise Exception("Wrong password.")
            
            return user_data
        except Exception as e:
            raise e

    
    