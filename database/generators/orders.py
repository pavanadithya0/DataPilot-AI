"""
Orders Generator
"""

import random

from faker import Faker
from sqlalchemy import insert

from database.connection import get_engine
from database.schema import orders
from utils.constants import ORDER_COUNT, REGIONS, SALES_REPS

fake = Faker()


def generate_orders():

    engine = get_engine()

    order_records = []

    for order_id in range(1, ORDER_COUNT + 1):

        order_records.append({

            "order_id": order_id,

            "customer_id": random.randint(1, 5000),

            "order_date": fake.date_between(
                start_date="-3y",
                end_date="today"
            ),

            "region": random.choice(REGIONS),

            "sales_rep": random.choice(SALES_REPS),

            "total_amount": 0

        })

    with engine.begin() as connection:

        connection.execute(

            insert(orders),

            order_records

        )

    print(f"✅ Inserted {ORDER_COUNT} orders.")