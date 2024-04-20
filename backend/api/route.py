from fastapi import FastAPI
from api.controllers import test
from api.controllers.user.controller import user_router
from api.controllers.auth.controller import auth_router
from api.controllers.category.controller import category_router
from api.__core__ import constants

def get_routes(app:FastAPI)->FastAPI:
    app.include_router(test.router, prefix=f"/api/{constants.APP_VERSION}/hello") 
    app.include_router(user_router, prefix=f"/api/{constants.APP_VERSION}/user")
    app.include_router(auth_router, prefix=f"/api/{constants.APP_VERSION}/auth")
    app.include_router(category_router, prefix=f"/api/{constants.APP_VERSION}/category")
    return app