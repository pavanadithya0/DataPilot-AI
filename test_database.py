from database.connection import create_database
from database.connection import get_engine
from sqlalchemy import inspect

create_database()

engine = get_engine()

inspector = inspect(engine)

print("Tables found:")
print(inspector.get_table_names())