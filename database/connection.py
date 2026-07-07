"""
Database Connection Module
"""

from pathlib import Path
from sqlalchemy import create_engine
from database.schema import metadata

# Project root
BASE_DIR = Path(__file__).resolve().parent.parent

# Absolute path to database
DB_PATH = BASE_DIR / "database" / "business.db"

print("Database path:", DB_PATH)
print("Database exists:", DB_PATH.exists())

DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(
    DATABASE_URL,
    echo=False,
)

def create_database():
    metadata.create_all(engine)
    print("✅ Database and tables created successfully.")

def get_engine():
    return engine