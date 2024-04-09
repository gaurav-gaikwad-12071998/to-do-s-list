


from todos.__db__.client import create_db, create_all_tables_async
from todos.__db__.table.user import UserTable
from todos.__db__.table.role import RoleTable

async def connect_db():
    await create_db()
    await create_all_tables_async()
    
    
