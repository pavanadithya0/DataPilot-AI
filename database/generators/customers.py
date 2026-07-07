"""
Customer Data Generator
-----------------------
Generates realistic customer records and inserts them into the database.
"""

import random
from faker import Faker
from sqlalchemy import insert

from database.connection import get_engine
from database.schema import customers
from utils.constants import CUSTOMER_COUNT, SEGMENTS

fake = Faker()


def generate_customers():
    """Generate customer records."""

    engine = get_engine()

    customer_records = []

    for customer_id in range(1, CUSTOMER_COUNT + 1):

        customer_records.append({
            "customer_id": customer_id,
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.unique.email(),
            "phone": fake.phone_number(),
            "city": fake.city(),
            "state": fake.state(),
            "segment": random.choice(SEGMENTS),
            "join_date": fake.date_between(
                start_date="-5y",
                end_date="today"
            )
        })

    from sqlalchemy import insert, select

    with engine.begin() as connection:
     connection.execute(insert(customers), customer_records)

print(f"✅ Inserted {CUSTOMER_COUNT} customers.")