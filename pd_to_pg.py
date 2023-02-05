import pandas as pg
from pandas.core.frame import DataFrame
import psycopg2 as pg
from io import StringIO

from config import pg_config

def pd_to_pg(df: DataFrame, tablename: str) -> None:
    """Push pandas dataframe into postgresql table"""
    
    sep = '\t'
    encoding = 'utf8'
    if_exists = 'fail'
    columns = tuple(df.columns)
    temp_output = StringIO()
    df.to_csv(
        temp_output,
        sep=sep,
        header = False,
        encoding = encoding,
        index=False
    )
    temp_output.seek(0)
    with pg.connect(
        dbname = pg_config.dbname,
        user = pg_config.user,
        password = pg_config.password,
        port = pg_config.port,
        options = pg_config.options
    ) as conn:
        with conn.cursor() as curr:
            try:
                curr.copy_from(
                    temp_output,
                    table = tablename,
                    columns = columns,
                    sep = sep,
                    null = ''
                )
            except pg.Error as err:
                raise err
