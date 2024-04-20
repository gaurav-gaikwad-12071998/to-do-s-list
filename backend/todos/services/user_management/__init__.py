import uuid
import datetime
from argon2 import PasswordHasher

from todos.__db__.table.user import UserTable
from todos.__db__.table.user_category import UserCategoryTable
from todos.__db__.table.role import RoleTable
from todos.__db__.table.category import CategoryTable
from todos.__core__ import constants
from todos.__core__.helper import standard_helper



class UserService:
    def __init__(
            self, 
            user_table: UserTable, 
            user_category_table: UserCategoryTable, 
            category_table: CategoryTable,
            role_table: RoleTable
        ):
        self.user_db_service = user_table
        self.user_category_db_service = user_category_table
        self.category_db_service = category_table
        self.role_db_service = role_table
        self.roles = None
        self.categories = None
    
    
        
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
                "user_birthdate": datetime.date.fromisoformat(user_birthdate),
                "role_id" : await self.get_role_id_by_title(role) # to get role id
            }
            
            
            insert_user_data = await self.user_db_service.insert(params)
        
            await self.map_default_category_by_user(insert_user_data[self.user_db_service.primary_key])

            return insert_user_data
            
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
        
    async def map_default_category_by_user(self, user_id:str):
        try:
            if(self.categories == None):
                self.categories = await self.category_db_service.get_by_query({"is_default" : True})
            
            for category_data in self.categories:
                user_category_params = {
                    "id" : uuid.uuid4(),
                    "user_id" : user_id,
                    "category_id" : category_data["category_id"]
                }
                await self.user_category_db_service.insert(user_category_params)
            
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
                raise Exception(constants.MESSAGES["USER_NOT_FOUND"])
            
            if(standard_helper.verify_password(user_data["password"], password) == False):
                raise Exception(constants.MESSAGES["WRONG_PASSWORD"])
            
            return user_data
        except Exception as e:
            raise e
    
    async def sign_up_user(self, user_name:str, user_email:str, user_password:str, confirm_password:str, user_contact:str, user_birthdate:str, role:str):
        user_data =  await self.create_user(user_name, user_email, user_password, confirm_password, user_contact, user_birthdate, role)
        if user_data == None:
            raise Exception(constants.MESSAGES["USER_NOT_CREATED"])
        else:         
            del user_data["password"]
            return user_data
    
    def allowed_user_edit(self, user_edit_params:dict):
        new_params = {}
        if "user_name" in user_edit_params and user_edit_params["user_name"] is not None:
            new_params["user_name"] = user_edit_params["user_name"]
        
        if "user_birthdate" in user_edit_params and user_edit_params["user_birthdate"] is not None:
            new_params["user_birthdate"] = user_edit_params["user_birthdate"]
            
        return new_params
            
    async def edit_user(self, user_id, user_edit_params:dict):
        try:
            user_data = await self.user_db_service.get_by_id(user_id)
            if (user_data is None):
                raise Exception(constants.MESSAGES["USER_NOT_FOUND"])
        
            new_user_edit_params = self.allowed_user_edit(user_edit_params)
            if(len(list(new_user_edit_params.keys())) > 0):
                return await self.user_db_service.update_by_id(user_id, new_user_edit_params)
            else:
                return 
        except Exception as e:
            raise e
        
    async def edit_sensitive_data(self, user_id, user_edit_params, password):
        try:
            user_data = await self.user_db_service.get_by_id(user_id)
            if (user_data is None):
                raise Exception(constants.MESSAGES["USER_NOT_FOUND"])
            
            if(standard_helper.verify_password(user_data["password"], password) == False):
                raise Exception(constants.MESSAGES["WRONG_PASSWORD"])
            
            return await self.user_db_service.update_by_id(user_id, user_edit_params)
        except Exception as e:
            raise e
        
    async def delete_user(self, user_id):
        try:
            user_data = await self.user_db_service.get_by_id(user_id)
            if (user_data is None):
                raise Exception(constants.MESSAGES["USER_NOT_FOUND"])
            
            return await self.user_db_service.delete_by_id(user_id)
        except Exception as e:
            raise e
    
        

    
    