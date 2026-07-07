DATABASE_SCHEMA = """
Tables:

customers
customer_id
first_name
last_name
email
phone
city
state
segment
join_date

products
product_id
product_name
category
sub_category
price
cost

orders
order_id
customer_id
order_date
region
sales_rep
total_amount

order_items
item_id
order_id
product_id
quantity
unit_price

payments
payment_id
order_id
payment_method
payment_status
amount

inventory
product_id
stock_quantity
warehouse
reorder_level
"""


def build_prompt(user_question):

    return f"""
You are an expert SQL developer.

Convert the following question into SQLite SQL.

Rules:

1. Return ONLY SQL.
2. Do NOT explain.
3. Only SELECT queries.
4. Never use DELETE.
5. Never use UPDATE.
6. Never use DROP.
7. Never use ALTER.

Database:

{DATABASE_SCHEMA}

Question:

{user_question}
"""