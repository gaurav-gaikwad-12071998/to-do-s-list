


DB_SALT = b'\xfe\xf5e\x8a\xf9n\x18\xff\xe9\xc4\xe6\x9b4\xa3}\x1e\xccrx\x1f\xb7\xbd\x0c4C\xfc\xfd\x88\x0e\x1e\xb8F'


ROLE = {
    "EDITOR": "editor",
    "ADMIN": "admin"
}

MESSAGES = {
    "USER_NOT_FOUND" : "User not found.",
    "WRONG_PASSWORD" : "Wrong password.",
    "USER_NOT_CREATED" : "User not created.",
    "CANNOT_DELETE_CATEGORY" : "Cannot delete default category"
}

DEFAULT_CATEGORIES = [
    "Important",  
    "Planned",
    "Personal", 
    'Work', 
    "Home", 
    "Finances", 
    "Health", 
    "Learning"
]

TABLE_NAME_MAPPER = {
    "ROLE": "role",
    "USER": "user",
    "CATEGORY": "category",
    "USER_CATEGORY": "user_category",
    "TASK": "task"
}

