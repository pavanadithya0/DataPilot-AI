"""
Inventory Generator
"""

import random

from sqlalchemy import insert

from database.connection import get_engine
from database.schema import inventory, products


WAREHOUSES = [
    "Hyderabad",
    "Bangalore",
    "Mumbai",
    "Chennai"
]


def generate_inventory():

    engine = get_engine()

    inventory_records = []

    with engine.connect() as connection:

        result = connection.execute(products.select())

        for product in result:

            inventory_records.append({

                "product_id": product.product_id,

                "stock_quantity": random.randint(20, 300),

                "warehouse": random.choice(WAREHOUSES),

                "reorder_level": random.randint(10, 40)

            })

    with engine.begin() as connection:

        connection.execute(

            insert(inventory),

            inventory_records

        )

    print(f"✅ Inserted {len(inventory_records)} inventory records.")