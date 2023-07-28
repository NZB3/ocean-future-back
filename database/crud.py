from sqlalchemy.sql import text, select
from sqlalchemy.ext.asyncio import AsyncSession

from database import models
from .schemas import CustomerCreate, AnimalsCreate, TicketsCreate


async def commiter(db):
    try:
        await db.commit()
    except Exception:
        await db.rollback()
        raise


async def get_customers(db: AsyncSession, limit: int):
    query = text(f"SELECT * FROM customers LIMIT {limit}")
    return await db.execute(query)


async def get_animals(db: AsyncSession, limit: int):
    query = text(f"SELECT * FROM animals LIMIT {limit}")
    return await db.execute(query)


async def get_tickets(db: AsyncSession, limit: int):
    query = text(f"SELECT * FROM tickets LIMIT {limit}")
    return await db.execute(query)


async def create_customer(db: AsyncSession, costumer: CustomerCreate):
    db_costumer = models.Customer(
        mail=costumer.mail,
        type=costumer.type,
        date=costumer.date,
        price=costumer.price,
        name=costumer.name,
        count=costumer.count,
        way_get=costumer.way_get
        )

    db.add(db_costumer)

    await commiter(db)

    return db_costumer


async def create_animals(db: AsyncSession, animal: AnimalsCreate):
    db_costumer = models.Animal(
        name=animal.name, description=animal.description
        )

    db.add(db_costumer)

    await commiter(db)

    return db_costumer


async def create_tickets(db: AsyncSession, ticket: TicketsCreate):
    db_costumer = models.Ticket(
        name=ticket.name, price=ticket.price, type=ticket.type
        )

    db.add(db_costumer)

    await commiter(db)

    return db_costumer
