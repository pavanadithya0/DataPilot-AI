FORBIDDEN = [
    "DROP",
    "DELETE",
    "UPDATE",
    "INSERT",
    "ALTER",
    "TRUNCATE",
    "CREATE"
]


def validate_sql(sql):

    sql_upper = sql.upper()

    for keyword in FORBIDDEN:

        if keyword in sql_upper:
            raise Exception(
                f"Forbidden SQL detected: {keyword}"
            )

    return True