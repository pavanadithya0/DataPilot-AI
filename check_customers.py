from database.connection import get_engine
from sqlalchemy import text

engine = get_engine()

with engine.connect() as conn:
    result = conn.execute(text("SELECT COUNT(*) FROM customers"))
    print("Customers:", result.scalar())