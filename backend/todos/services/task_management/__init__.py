import uuid
from todos.__db__.table.task import TaskTable

class TaskService:
    
    def __init__(self, task_table: TaskTable):
        self.task_db_service = task_table
        
    async def create_task(self, task_title, task_description, category_id, task_due, task_status, task_priority, user_id):
        try:
            params = {
                self.task_db_service.primary_key : str(uuid.uuid4()),
                "task_title" : task_title,
                "task_description" : task_description,
                "category_id" : category_id,
                "task_due" : task_due,
                "task_status" : task_status,
                "task_priority" : task_priority,
                "user_id" : user_id
            }
            return await self.task_db_service.insert(params)
        
        except Exception as e:
            raise e
        
    async def get_all_tasks(self):
        try:
            return await self.task_db_service.get_all()
        except Exception as e:
            raise e
    
    async def get_task_by_id(self, task_id:str):
        try:
            return await self.task_db_service.get_by_id(task_id)
        except Exception as e:
            raise e
        
    async def get_tasks_by_user_id(self, user_id:str):
        try:
            return await self.task_db_service.get_by_query({"user_id": user_id})
        except Exception as e:
            raise e
        
    async def update_task_by_id(self, task_id:str, updated_data:dict):
        try:    
            return await self.task_db_service.update_by_id(task_id, updated_data)
        except Exception as e:
            raise e
    
    async def delete_task_by_id(self, task_id:str):
        try:
            return await self.task_db_service.delete_by_id(task_id)
        except Exception as e:
            raise e
    