
import uuid

from todos.__db__.table.category import CategoryTable
from todos.__db__.table.user_category import UserCategoryTable
from todos.__db__.table.user import UserTable
from todos.__core__ import constants


class CategoryService:
    def __init__(self, category_table: CategoryTable, user_category_table: UserCategoryTable, user_table: UserTable):
        self.category_db_service = category_table
        self.user_category_db_service = user_category_table
        self.user_db_service = user_table
        
    async def create_category(self, category_title, is_default = False):
        try:
            
            params = {
                self.category_db_service.primary_key : str(uuid.uuid4()),
                "category_title": category_title,
                "is_default" : is_default
            }
            return await self.category_db_service.insert(params)
        except Exception as e:
            raise e
        
    async def create_default_categories(self):
        try:
            for category in constants.DEFAULT_CATEGORIES:
                category_data = await self.category_db_service.get_by_query({"category_title": category})

                if(len(category_data) == 0):
                    await self.create_category(category, True)
                    
        except Exception as e:
            raise e
        
    async def create_category_for_user(self, user_id, category_title):
        try:
            user_data = self.user_db_service.get_by_id(user_id)
            if user_data is None :
                raise Exception(constants.MESSAGES["USER_NOT_FOUND"])
            
            category_data = await self.create_category(category_title)
            
            user_category_params = {
                "user_id" : user_id,
                "category_id" : category_data[self.category_db_service.primary_key]
            }
            await self.user_category_db_service.insert(user_category_params)
            
            del category_data["is_default"]
            return category_data
            
        except Exception as e:
            raise e
        
    async def get_all_categories(self):
        try:
            return await self.category_db_service.get_all()
        except Exception as e:
            raise e
        
    
    async def get_categories_by_user(self, user_id:str):
        return await self.user_category_db_service.get_by_user_id(user_id)
        
    async def delete_category_for_user(self, user_id, category_title, category_id):
        try:
            if category_title in constants.DEFAULT_CATEGORIES:
                raise Exception(constants.MESSAGES["CANNOT_DELETE_CATEGORY"])
            
            # delete from user category
            await self.user_category_db_service.delete_by_user_id_and_category_id(user_id, category_id)
            
            # # get category by user and category
            # user_category_data = await self.user_category_db_service.get_by_user_id_and_category(user_id, category_title)
            
            # if(len(user_category_data) > 0):
            #     await self.user_category_db_service.
            
            # category_id = user_category_data["category_id"]
            
            # await self.user_category_db_service.delete_by_id(category_id)
            
            # return await self.category_db_service.delete_by_id(category_id)
        except Exception as e:
            raise e
        