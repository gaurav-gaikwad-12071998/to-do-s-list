from todos.__db__.schema import Base
from todos.__db__.client import engine, SessionLocal
from sqlalchemy import text, Result, select, Executable

class DatabaseService():
    
    def __init__(self, table):
        self.engine = engine
        self.session = SessionLocal
        self.base = Base
        self.table_class = table
        
    
            
    async def execute_query(self, query:any, params:dict={}, return_value:bool=False):
        try:
            session = self.session()
            raw_sql = text(query)
            
            if(len(params) == 0):
                results:Result = await session.execute(raw_sql)
            else:
                results:Result = await session.execute(raw_sql, params)
              
            if(return_value):
                results = [result._asdict() for result in results]
                
            await session.commit()    
            return results
        except Exception as e:
            await session.rollback()
            raise Exception(e)
        finally:
            await session.close()
    
    
    async def get_all(self):
        query = f'''
            SELECT * 
            FROM public.{self.table_class.__tablename__}
        '''
        return await self.execute_query(query, return_value=True)
    
    
    