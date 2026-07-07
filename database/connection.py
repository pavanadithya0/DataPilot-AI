"""
Database Connection Module
--------------------------
This module is responsible for:
1. Creating the SQLite database engine.
2. Creating all tables defined in schema.py.
3. Providing a reusable database connection.
"""

from sqlalchemy import create_engine
from database.schema import metadata
import os
# SQLite database file
DATABASE_URL = "sqlite:///database/business.db"

# Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    echo=False
)
print("Database path:", os.path.abspath("database/business.db"))


def create_database():
    """
    Create all database tables.
    This function is safe to call multiple times.
    """
    metadata.create_all(engine)
    print("✅ Database and tables created successfully.")


def get_engine():
    """
    Returns the SQLAlchemy engine.
    """
    return engine