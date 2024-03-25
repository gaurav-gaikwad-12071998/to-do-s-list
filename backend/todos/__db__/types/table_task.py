from typing import TypedDict
from datetime import datetime

class taskInsertParams(TypedDict):
    task_id : str
    task_title : str
    task_description : str
    category_id : str
    task_due : datetime
    task_status : str
    task_priority : str
    user_id : str
