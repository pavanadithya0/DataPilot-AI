"""
Order Items Generator
"""

import random

from sqlalchemy import insert, select, update

from database.connection import get_engine
from database.schema import (
    products,
    orders,
    order_items
)


def generate_order_items():

    engine = get_engine()

    item_records = []

    item_id = 1

    with engine.begin() as connection:

        all_products = connection.execute(
            select(products)
        ).fetchall()

        all_orders = connection.execute(
            select(orders)
        ).fetchall()

        for order in all_orders:

            total = 0

            # Each order has 1–5 products
            selected_products = random.sample(
                all_products,
                random.randint(1, 5)
            )

            for product in selected_products:

                quantity = random.randint(1, 4)

                unit_price = product.price

                total += quantity * unit_price

                item_records.append({

                    "item_id": item_id,

                    "order_id": order.order_id,

                    "product_id": product.product_id,

                    "quantity": quantity,

                    "unit_price": unit_price

                })

                item_id += 1

            connection.execute(

                update(orders)
                .where(
                    orders.c.order_id == order.order_id
                )
                .values(total_amount=round(total, 2))

            )

        connection.execute(

            insert(order_items),

            item_records

        )

    print(f"✅ Inserted {len(item_records)} order items.")