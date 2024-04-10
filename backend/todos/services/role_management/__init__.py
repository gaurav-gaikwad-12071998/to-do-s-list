import uuid
from todos.__db__.table.role import RoleTable

class RoleService:
    def __init__(self, role_table: RoleTable):
        self.role_db_service = role_table
        
    async def create_role(self, role_title, role_description):
        try:
            
            params = {
                self.role_db_service.primary_key : str(uuid.uuid4()),
                "role_title": role_title,
                "role_description": role_description
            }
            return await self.role_db_service.insert(params)
        except Exception as e:
            if ('unique constraint "role_role_title_key"' in str(e)):
                print(f"{role_title} already created.")
            else:
                raise e
        
    async def create_roles(self):
        try:
            # editor role
            await self.create_role("EDITOR", "Editor role")
            # admin role
            await self.create_role("ADMIN", "Admin role")
            
            print("Roles created successfully.")
        except Exception as e:
            raise e  
        
    async def get_roles(self):
        try:
            return await self.role_db_service.get_all()
        except Exception as e:
            raise e
            
            