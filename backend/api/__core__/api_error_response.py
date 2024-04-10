from fastapi import FastAPI, HTTPException, status

class UserNotFound(HTTPException):
    def __init__(self, detail="User not found."):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail = detail)

class WrongEmailOrPassword(HTTPException):
    def __init__(self, detail="Wrong email or password."):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail = detail)

class InternalServerError(HTTPException):
    def __init__(self, detail="Something went wrong."):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail = detail)

app = FastAPI()