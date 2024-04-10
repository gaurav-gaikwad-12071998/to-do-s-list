

from todos.__db__.table.category import CategoryTable

class CategoryService:
    def __init__(self, category_table: CategoryTable):
        self.category_db_service = category_table