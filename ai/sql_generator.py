import re
from ai.llm import ask_gemini


# --------------------------------------------------
# Clean Gemini SQL
# --------------------------------------------------

def clean_sql(sql: str) -> str:
    """
    Cleans Gemini response and returns executable SQL.
    """

    if not sql:
        return ""

    # Remove markdown
    sql = re.sub(r"```sql", "", sql, flags=re.IGNORECASE)
    sql = re.sub(r"```sqlite", "", sql, flags=re.IGNORECASE)
    sql = sql.replace("```", "")

    # Keep SQL only
    match = re.search(
        r"(SELECT|INSERT|UPDATE|DELETE|WITH)\b.*",
        sql,
        flags=re.IGNORECASE | re.DOTALL,
    )

    if match:
        sql = match.group(0)

    return sql.strip()


# --------------------------------------------------
# Generate SQL
# --------------------------------------------------

def generate_sql(question: str) -> str:
    """
    Converts natural language into SQLite SQL.

    First checks predefined templates.
    If no template matches, Gemini is used.
    """

    q = question.lower().strip()

    # ==================================================
    # LOCAL SQL TEMPLATES (NO GEMINI REQUIRED)
    # ==================================================

    if "top" in q and "customer" in q and "revenue" in q:

        return """
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    SUM(o.total_amount) AS total_revenue
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name
ORDER BY total_revenue DESC
LIMIT 10;
"""

    elif "payment" in q:

        return """
SELECT
    payment_method,
    COUNT(*) AS payment_count
FROM payments
GROUP BY payment_method
ORDER BY payment_count DESC;
"""

    elif "monthly revenue" in q:

        return """
SELECT
    strftime('%Y-%m', order_date) AS month,
    SUM(total_amount) AS revenue
FROM orders
GROUP BY month
ORDER BY month;
"""

    elif "orders by region" in q:

        return """
SELECT
    region,
    COUNT(*) AS total_orders
FROM orders
GROUP BY region
ORDER BY total_orders DESC;
"""

    elif "top selling products" in q:

        return """
SELECT
    p.product_name,
    SUM(oi.quantity) AS total_sold
FROM order_items oi
JOIN products p
ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC
LIMIT 10;
"""

    elif "revenue by state" in q:

        return """
SELECT
    c.state,
    SUM(o.total_amount) AS revenue
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY c.state
ORDER BY revenue DESC;
"""

    elif "inventory" in q or "reorder" in q:

        return """
SELECT
    product_id,
    stock_quantity,
    reorder_level,
    warehouse
FROM inventory
WHERE stock_quantity < reorder_level;
"""

    # ==================================================
    # GEMINI FALLBACK
    # ==================================================

    prompt = f"""
You are an expert SQLite SQL generator.

Database Tables

customers
(customer_id, first_name, last_name, email, phone, city, state, segment, join_date)

products
(product_id, product_name, category, sub_category, price, cost)

orders
(order_id, customer_id, order_date, region, sales_rep, total_amount)

order_items
(item_id, order_id, product_id, quantity, unit_price)

payments
(payment_id, order_id, payment_method, payment_status, amount)

inventory
(product_id, stock_quantity, warehouse, reorder_level)

Rules:

1. Return ONLY executable SQLite SQL.
2. Do NOT use markdown.
3. Do NOT explain anything.
4. Response must start with SELECT or WITH.

Question:
{question}
"""

    try:

        sql = ask_gemini(prompt)

        return clean_sql(sql)

    except Exception:

        raise Exception(
            "Gemini quota exceeded. Try one of the predefined example questions from the sidebar."
        )