
from todos.__db__.schema import Category
from todos.__db__.database import DatabaseService
from todos.__db__.types.table_category import categoryInsertParams
from uuid import uuid4




class CategoryTable(DatabaseService):
    
    def __init__(self, table_class: Category):
        super().__init__(table_class)
        self.primary_key = "category_id"
        
    async def insert(self, category_params:categoryInsertParams):
        session = self.session()
        try:
            new_category = self.table_class(**category_params)
            session.add(new_category)
            await session.commit()
            return category_params
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