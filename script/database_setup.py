from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# Get credentials from the environment
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

def create_db_engine():
    """
    Creates an SQLAlchemy engine for PostgreSQL using environment variables.

    :return: SQLAlchemy engine instance.
    """
    try:
        db_url = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        engine = create_engine(db_url)
        print("Database engine created successfully!")
        return engine
    except Exception as e:
        print(f"An error occurred while creating the database engine: {e}")
        return None

def load_data_from_db(query, engine):
    """
    Loads data from PostgreSQL database using a SQLAlchemy engine and SQL query.

    :param query: SQL query to execute.
    :param engine: SQLAlchemy engine object.
    :return: DataFrame containing the results of the query.
    """
    try:
        df = pd.read_sql_query(query, engine)
        print("Data loaded successfully!")
        return df
    except Exception as e:
        print(f"An error occurred while loading data: {e}")
        return None
def export_data_to_postgres(df, table_name, engine):
    """
    Exports a DataFrame to a PostgreSQL database as a table using a SQLAlchemy engine.

    :param df: DataFrame to export.
    :param table_name: Name of the PostgreSQL table to create/replace.
    :param engine: SQLAlchemy engine object.
    """
    try:
        df.to_sql(table_name, engine, index=False, if_exists='replace')
        print(f"Data exported successfully to table '{table_name}'!")
    except Exception as e:
        print(f"An error occurred while exporting data: {e}")