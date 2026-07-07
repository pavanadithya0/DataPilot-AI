from sqlalchemy import text
from database.connection import get_engine


def get_kpis():
    engine = get_engine()

    with engine.connect() as conn:

        total_customers = conn.execute(
            text("SELECT COUNT(*) FROM customers")
        ).scalar()

        total_orders = conn.execute(
            text("SELECT COUNT(*) FROM orders")
        ).scalar()

        total_revenue = conn.execute(
            text("SELECT SUM(total_amount) FROM orders")
        ).scalar()

        avg_order = conn.execute(
            text("SELECT AVG(total_amount) FROM orders")
        ).scalar()

    return {
        "customers": total_customers,
        "orders": total_orders,
        "revenue": total_revenue,
        "avg_order": avg_order,
    }