from fastapi import FastAPI

from database.main import db_router


app = FastAPI()


app.include_router(db_router)
