"""
Database Seeder
---------------
Drops all tables, recreates them, and seeds fresh data.
"""

from database.connection import get_engine
from database.schema import metadata

from database.generators.customers import generate_customers
from database.generators.products import generate_products
from database.generators.inventory import generate_inventory
from database.generators.orders import generate_orders
from database.generators.order_items import generate_order_items
from database.generators.payments import generate_payments
def seed_database():

    engine = get_engine()

    print("Dropping existing tables...")
    metadata.drop_all(engine)

    print("Creating new tables...")
    metadata.create_all(engine)

    print("Generating Customers...")
    generate_customers()

    print("Generating Products...")
    generate_products()

    print("Generating Inventory...")
    generate_inventory()

    print("Generating Orders...")
    generate_orders()

    print("Generating Order Items...")
    generate_order_items()

    print("Generating Payments...")
    generate_payments()

    print("\nDatabase seeding completed successfully!")


if __name__ == "__main__":
    seed_database()