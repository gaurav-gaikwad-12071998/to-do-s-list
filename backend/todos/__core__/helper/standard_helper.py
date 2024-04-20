from argon2 import PasswordHasher

from todos.__core__ import constants

password_hasher: PasswordHasher = PasswordHasher()

def hash_password( user_password):
    return password_hasher.hash(user_password.encode(), salt=constants.DB_SALT)
        
def verify_password( hashed_password, user_input_password):
    try:
        password_hasher.verify(hashed_password, user_input_password)
        return True
    except:
        return False

def is_subset(list1, list2):
  return all(element in list1 for element in list2)