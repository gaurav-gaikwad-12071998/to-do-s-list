
from uuid import uuid4

from todos.__db__.schema import UserCategory
from todos.__db__.database import DatabaseService
from todos.__db__.types.table_user_category import user_categoryInsertParams
from todos.__core__ import constants




class UserCategoryTable(DatabaseService):
    
    def __init__(self, table_class:UserCategory):
        super().__init__(table_class)
        self.primary_key = "user_category_id"
        
    async def insert(self, user_category_params:user_categoryInsertParams):
        session = self.session()
        try:
            new_user_category = self.table_class(**user_category_params)
            session.add(new_user_category)
            await session.commit()
            return user_category_params
        except Exception as e:
            print(e)
            await session.rollback()
            raise e
        finally:
            await session.close()
            
    async def get_by_id(self, id:str):
        try:
            query = f'''
                SELECT * 
                FROM public.{self.table_class.__tablename__}
                WHERE {self.primary_key} = :{self.primary_key}
            '''
            params = {
                self.primary_key : id
            }
            result = await self.execute_query(query, params, return_value=True)
            return result[0]
        except Exception as e:
            raise e
    
    async def get_by_user_id(self, user_id:str, is_default:bool = False):
        try:
            category_table = constants.TABLE_NAME_MAPPER["CATEGORY"]
            query = f'''
                SELECT uc.user_id, uc.category_id, c.category_title 
                FROM {self.table_class.__tablename__} uc
                INNER JOIN {category_table} c ON c.category_id = uc.category_id
                WHERE uc.user_id = :user_id and c.is_default = :is_default;
            '''
            params = {
                "user_id" : user_id,
                "is_default": is_default
            }
            
            result = await self.execute_query(query, params, return_value=True)
            return result[0]
        except Exception as e:
            raise e
    
    async def get_by_user_id_and_category(self, user_id:str, category_title:str):
        try:
            category_table = constants.TABLE_NAME_MAPPER["CATEGORY"]
            query = f'''
                SELECT uc.id, uc.user_id, uc.category_id, c.category_title 
                FROM {self.table_class.__tablename__} uc
                INNER JOIN {category_table} c ON c.category_id = uc.category_id
                WHERE uc.user_id = :user_id and c.category_title = :category_title;
            '''
            params = {
                "user_id" : user_id,
                "category_title": category_title
            }
            
            result = await self.execute_query(query, params, return_value=True)
            return result[0]
        except Exception as e:
            raise e
    
   
    async def update_by_id(self, id:str, updated_data:dict):
        try:
            if(self.primary_key in updated_data):
                del updated_data[self.primary_key]
            
            set_clause = list(map(lambda x: x+" = :"+x, list(updated_data.keys())))
            query = f'''
                UPDATE public.{self.table_class.__tablename__}
                SET {", ".join(set_clause)}
                WHERE {self.primary_key} = :{self.primary_key} 
                RETURNING *
            '''
        
            params = {
                self.primary_key : id,
                **updated_data
            }
            
            return await self.execute_query(query, params, return_value=True)
        except Exception as e:
            raise e
        
    async def delete_by_id(self, id:str):
        try:
            query = f'''
                DELETE FROM public.{self.table_class.__tablename__}
                WHERE {self.primary_key} = :{self.primary_key} 
            '''
            params = {
                self.primary_key : id
            }
            
            return await self.execute_query(query, params)
        except Exception as e:
            raise e
        
    async def delete_by_user_id_and_category_id(self, user_id:str, category_id:str):
        try:
            query = f'''
                DELETE FROM public.{self.table_class.__tablename__}
                WHERE user_id = :{user_id} and category_id = :{category_id}
            '''
            params = {
                "user_id" : user_id,
                "category_id" : category_id
            }
            
            return await self.execute_query(query, params)
        except Exception as e:
            raise e
        
    async def get_all(self):
        try:
            query = f'''
                SELECT * EXCLUDE ( password )
                FROM public.{self.table_class.__tablename__}
            '''
            return await self.execute_query(query, return_value=True)
        except Exception as e:
            raise e
        
