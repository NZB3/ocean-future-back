from typing import List

from fastapi import APIRouter

from database import crud
from .base import db
from .schemas import CustomerCreate, AnimalsCreate, TicketsCreate


db_router = APIRouter(tags=["database"])


@db_router.on_event("startup")
async def startup_event():
    db_router._db = db
    db_router._db.init()
    await db_router._db.create_all()



@db_router.get("/database")
async def main():
    return {"router": "database"}


@db_router.post("/database/customers/")
async def create_customer(costumer: CustomerCreate):
    return await crud.create_customer(db_router._db, costumer)


@db_router.get("/database/customers/", response_model=List[CustomerCreate])
async def get_customer(limit: int = 20):
    customer_list = await crud.get_customers(db_router._db, limit)
    return customer_list.all()


@db_router.post("/database/animals/")
async def create_animals(animal: AnimalsCreate):
    return await crud.create_animals(db_router._db, animal)


@db_router.get("/database/animals/", response_model=List[AnimalsCreate])
async def get_animals(limit: int = 20):
    animal_list = await crud.get_animals(db_router._db, limit)
    return animal_list.all()


@db_router.post("/database/tickets/")
async def create_tickets(ticket: TicketsCreate):
    return await crud.create_tickets(db_router._db, ticket)


@db_router.get("/database/tickets/", response_model=List[TicketsCreate])
async def get_tickets(limit: int = 20):
    ticket_list = await crud.get_tickets(db_router._db, limit)
    return ticket_list.all()
