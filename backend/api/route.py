from fastapi import FastAPI
from api.controllers import test
from api.__core__ import constants

def get_routes(app:FastAPI)->FastAPI:
    app.include_router(test.router, prefix=f"/api/{constants.APP_VERSION}/hello") 
    return app