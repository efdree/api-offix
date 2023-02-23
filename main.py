from fastapi import FastAPI
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.employee import employee_router
from routers.department import department_router

app = FastAPI()
app.title = "Offix API"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)

app.include_router(employee_router)
app.include_router(department_router)

Base.metadata.create_all(bind=engine)
