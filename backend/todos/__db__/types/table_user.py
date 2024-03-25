from typing import TypedDict


class userInsertParams(TypedDict):
    user_id : str
    user_name : str
    user_contact : str
    user_email : str
    user_birthdate: str
    role_id : str
    verified : bool
    password : str
