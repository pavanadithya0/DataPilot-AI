"""
Product Generator
"""

import random

from sqlalchemy import insert

from database.connection import get_engine
from database.schema import products
from utils.constants import PRODUCT_CATEGORIES


def generate_products():

    engine = get_engine()

    product_records = []

    product_id = 1

    for category, product_list in PRODUCT_CATEGORIES.items():

        for product_name in product_list:

            cost = round(random.uniform(20, 500), 2)

            price = round(cost * random.uniform(1.25, 2.0), 2)

            product_records.append({

                "product_id": product_id,

                "product_name": product_name,

                "category": category,

                "sub_category": category,

                "price": price,

                "cost": cost

            })

            product_id += 1

    with engine.begin() as connection:

        connection.execute(

            insert(products),

            product_records

        )

    print(f"✅ Inserted {len(product_records)} products.")