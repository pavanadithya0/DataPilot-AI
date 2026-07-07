import pandas as pd

from sqlalchemy import text

from database.connection import get_engine


engine = get_engine()


def execute_sql(sql):

    with engine.connect() as connection:

        df = pd.read_sql(
            text(sql),
            connection
        )

    return df