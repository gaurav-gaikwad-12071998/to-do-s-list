


from todos.__db__.client import create_db, create_all_tables_async
from todos.__db__.dependancy_injection import Container

database = Container()
async def connect_db():
    await create_db()
    await create_all_tables_async()
    

DatabaseService = database.database_service
Category = database.category
CategoryTable = database.category_table
Role = database.role
RoleTable = database.role_table
Task = database.task
TaskTable = database.task_table
UserCategory= database.user_category
UserCategoryTable = database.user_category_table
User = database.user
UserTable = database.user_table

