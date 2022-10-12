

class pg_config:
    """helper class for postgresql config params"""
    host = 'localhost'
    port = 5432
    dbname = 'postgres'
    user = 'postgres'
    password = 'postgres'
    options = '-c search_path=public'
    autocommit = True
