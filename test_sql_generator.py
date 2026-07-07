from ai.sql_generator import generate_sql

question = "Show top 10 customers by total purchase amount"

sql = generate_sql(question)

print(sql)