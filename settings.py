import psycopg2
from psycopg2 import sql
from config import load_config_from_env

def database_exists(database_name, user, password, host="localhost"):
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
    )
    connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()
    cursor.execute(
        sql.SQL("SELECT 1 FROM pg_database WHERE datname = {}").format(
            sql.Literal(database_name)  # Use sql.Literal to properly format string literals
        )
    )
    exists = cursor.fetchone()
    cursor.close()
    connection.close()
    return exists is not None


def create_database(database_name, user, password, host="localhost"):
    db_params = {
        'host': host,
        'port': '5432',
        'user': user,
        'password': password,
    }
    connection = psycopg2.connect(**db_params)
    connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()

    # CREATE DATABASE statement
    cursor.execute(
        sql.SQL("CREATE DATABASE {}").format(sql.Identifier(database_name))
    )

    # GRANT privileges
    cursor.execute(
        sql.SQL("GRANT ALL PRIVILEGES ON DATABASE {} TO {}").format(
            sql.Identifier(database_name), sql.Identifier(user)
        )
    )

    cursor.close()
    connection.close()


if __name__ == "__main__":
    config = load_config_from_env()

    if not database_exists(config.database_name, config.user, config.password, config.host):
        create_database(config.database_name, config.user, config.password, config.host)
    else:
        print(f"Database '{config.database_name}' already exists.")
