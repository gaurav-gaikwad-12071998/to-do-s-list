
from todos.__db__.schema import Role
from todos.__db__.database import DatabaseService
from todos.__db__.types.table_role import roleInsertParams
from uuid import uuid4




class RoleTable(DatabaseService):
    
    def __init__(self):
        super().__init__(Role)
        self.primary_key = "role_id"
        
    async def insert(self, role_params:roleInsertParams):
        session = self.session()
        try:
            new_role = self.table_class(**role_params)
            session.add(new_role)
            await session.commit()
        except Exception as e:
            print(e)
            await session.rollback()
        finally:
            await session.close()
            
    async def get_by_id(self, id:str):
        
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
    
   
    async def update_by_id(self, id:str, updated_data:dict):
        
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
    
    async def delete_by_id(self, id:str):
        
        query = f'''
            DELETE FROM public.{self.table_class.__tablename__}
            WHERE {self.primary_key} = :{self.primary_key} 
        '''
        params = {
            self.primary_key : id
        }
        
        return await self.execute_query(query, params)