
import asyncio
from fastapi import Depends, FastAPI
# from api.controllers import translate, at_translate
from fastapi.middleware.cors import CORSMiddleware
from api.route import get_routes
from api.tags import tags_metadata

from todos import connect_db
from todos import RoleService, CategoryService
async def lifespan(app: FastAPI):
    await connect_db()
    role_service = RoleService()
    category_service = CategoryService()
    await role_service.create_roles()
    await category_service.create_default_categories()
    yield
    

app = FastAPI(
    title="FastAPI with Swagger UI Example",
    description="A simple FastAPI example with Swagger UI for documentation",
    lifespan=lifespan,
    openapi_tags= tags_metadata
)

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://127.0.0.1",
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

# # Add CORS middleware to the application
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "PUT", "DELETE"],
#     allow_headers=["Authorization", "Content-Type"],
# )


app = get_routes(app)

# app.include_router(translate.router, prefix="/api/v1/translate")
# app.include_router(at_translate.router, prefix="/api/v1/translate/authoring")
# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=5001)