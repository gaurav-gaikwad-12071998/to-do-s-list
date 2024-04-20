
from todos.__db__.schema import Task
from todos.__db__.database import DatabaseService
from todos.__db__.types.table_task import taskInsertParams
from uuid import uuid4




class TaskTable(DatabaseService):
    
    def __init__(self, table_class:Task):
        super().__init__(table_class)
        self.primary_key = "task_id"
        
    async def insert(self, task_params:taskInsertParams):
        session = self.session()
        try:
            new_task = self.table_class(**task_params)
            session.add(new_task)
            await session.commit()
        except Exception as e:
            await session.rollback()
            raise e
        finally:
            await session.close()
    
    async def insert_all(self, data_list: list[dict]):
        session = self.db()
        try:
            # Use add_all for bulk insertion
            session.add_all([self.table_class(**item) for item in data_list])
            await session.commit()
        except Exception as e:
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