import pandas as pd
import psycopg2 as pg
from pandas.core.frame import DataFrame

from config import pg_config

def pg_to_pd(sql: str) -> DataFrame:
    """Load pandas DataFrame from raw sql query"""
    
    with pg.connect(
        dbname = pg_config.dbname,
        user = pg_config.user,
        password = pg_config.password,
        port = pg_config.port,
        options = pg_config.options
    ) as conn:
        with conn.cursor() as curr:
            try:
                curr.execute(sql)
                cols = list(map(lambda x: x[0], curr.description))
                df = pd.DataFrame(curr.fetchall(), columns=cols)
                return df
            except pg.Error as err:
                return err