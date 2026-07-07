from ai.sql_generator import generate_sql
from ai.sql_executor import execute_sql

question = "Show top 10 customers by total purchase amount"

sql = generate_sql(question)

print("\nGenerated SQL:\n")
print(sql)

df = execute_sql(sql)

print("\nResults:\n")
print(df.head())