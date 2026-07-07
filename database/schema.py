
from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Float,
    Date,
    ForeignKey,
)

metadata = MetaData()

# ----------------------------
# Customers Table
# ----------------------------
customers = Table(
    "customers",
    metadata,

    Column("customer_id", Integer, primary_key=True),
    Column("first_name", String(50), nullable=False),
    Column("last_name", String(50), nullable=False),
    Column("email", String(100), unique=True),
    Column("phone", String(20)),
    Column("city", String(50)),
    Column("state", String(50)),
    Column("segment", String(30)),
    Column("join_date", Date)
)

# ----------------------------
# Products Table
# ----------------------------
products = Table(
    "products",
    metadata,

    Column("product_id", Integer, primary_key=True),
    Column("product_name", String(100), nullable=False),
    Column("category", String(50)),
    Column("sub_category", String(50)),
    Column("price", Float),
    Column("cost", Float)
)

# ----------------------------
# Orders Table
# ----------------------------
orders = Table(
    "orders",
    metadata,

    Column("order_id", Integer, primary_key=True),
    Column(
        "customer_id",
        Integer,
        ForeignKey("customers.customer_id")
    ),
    Column("order_date", Date),
    Column("region", String(50)),
    Column("sales_rep", String(50)),
    Column("total_amount", Float)
)

# ----------------------------
# Order Items Table
# ----------------------------
order_items = Table(
    "order_items",
    metadata,

    Column("item_id", Integer, primary_key=True),
    Column(
        "order_id",
        Integer,
        ForeignKey("orders.order_id")
    ),
    Column(
        "product_id",
        Integer,
        ForeignKey("products.product_id")
    ),
    Column("quantity", Integer),
    Column("unit_price", Float)
)

# ----------------------------
# Payments Table
# ----------------------------
payments = Table(
    "payments",
    metadata,

    Column("payment_id", Integer, primary_key=True),
    Column(
        "order_id",
        Integer,
        ForeignKey("orders.order_id")
    ),
    Column("payment_method", String(30)),
    Column("payment_status", String(20)),
    Column("amount", Float)
)

# ----------------------------
# Inventory Table
# ----------------------------
inventory = Table(
    "inventory",
    metadata,

    Column(
        "product_id",
        Integer,
        ForeignKey("products.product_id"),
        primary_key=True
    ),
    Column("stock_quantity", Integer),
    Column("warehouse", String(50)),
    Column("reorder_level", Integer)
)
