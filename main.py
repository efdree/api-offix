from fastapi import FastAPI
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.employee import employee_router
from routers.department import department_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.title = "Offix API"
app.version = "0.0.1"

origins = [
    "http://localhost:8000",
    "http://localhost:3000"
]

app.add_middleware(ErrorHandler)
app.add_middleware(CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
                   )
app.include_router(employee_router)
app.include_router(department_router)

Base.metadata.create_all(bind=engine)
