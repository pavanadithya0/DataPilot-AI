"""
Payments Generator
"""

import random

from sqlalchemy import insert, select

from database.connection import get_engine
from database.schema import orders, payments
from utils.constants import PAYMENT_METHODS, PAYMENT_STATUS


def generate_payments():

    engine = get_engine()

    payment_records = []

    with engine.begin() as connection:

        all_orders = connection.execute(
            select(orders)
        ).fetchall()

        payment_id = 1

        for order in all_orders:

            payment_records.append({

                "payment_id": payment_id,

                "order_id": order.order_id,

                "payment_method": random.choice(PAYMENT_METHODS),

                "payment_status": random.choices(
                    PAYMENT_STATUS,
                    weights=[90, 7, 3],
                    k=1
                )[0],

                "amount": order.total_amount

            })

            payment_id += 1

        connection.execute(
            insert(payments),
            payment_records
        )

    print(f"✅ Inserted {len(payment_records)} payments.")