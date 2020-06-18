"""DB file."""
from typing import Any

import sqlalchemy as sa

from aiopg.sa import create_engine

metadata = sa.MetaData()

delivery_status = sa.Table('delivery_status', metadata,
                           sa.Column('identifier', sa.VARCHAR,
                                     nullable=False,
                                     primary_key=True,
                                     comment='unique goods identifier'),
                           sa.Column('status', sa.VARCHAR,
                                     nullable=False,
                                     comment='delivery status')
                           )


async def create_table(engine: Any) -> None:
    """Create table delivery_status if not exist."""
    async with engine.acquire() as conn:
        await conn.execute('''CREATE TABLE IF NOT EXISTS delivery_status (
                                      identifier varchar(255) NOT NULL PRIMARY KEY,
                                      status varchar(255) NOT NULL)''')


async def insert_or_update(d_id: str, d_status: str) -> None:
    """Insert or update data to delivery_status table."""
    async with create_engine(user='postgres',
                             database='postgres',
                             host='127.0.0.1',
                             port="5432",
                             password='123') as engine:
        await create_table(engine)
        async with engine.acquire() as conn:
            result = False
            async for row in conn.execute(delivery_status.select().where(delivery_status.c.identifier == d_id)):
                result = row.identifier
            if result == str(d_id):
                await conn.execute(delivery_status.update().where(delivery_status.c.identifier == d_id).
                                   values(status=d_status))
            else:
                await conn.execute(delivery_status.insert().values(identifier=d_id,
                                                                   status=d_status))
            async for row in conn.execute(delivery_status.select().where(delivery_status.c.identifier == d_id)):
                print(row.identifier, row.status)


async def get_info() -> str:
    """Select data from table delivery_status."""
    result = ""
    async with create_engine(user='postgres',
                             database='postgres',
                             host='127.0.0.1',
                             port="5432",
                             password='123') as engine:
        await create_table(engine)
        async with engine.acquire() as conn:
            async for row in conn.execute(delivery_status.select()):
                result += f"Идентификатор: {row.identifier}, статус заказа: {row.status}\n"
            return result
