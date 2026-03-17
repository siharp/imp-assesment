import clickhouse_connect
from sqlalchemy import create_engine
import pandas as pd


# -------------------
# EXTRACT
# -------------------
def extract_data(engine, query):
    print("🔄 Extracting data...")
    df = pd.read_sql(query, engine)
    print(f"✅ Extracted {len(df)} rows")
    return df


# -------------------
# TRANSFORM
# -------------------
def transform(data):
    print("🔄 Transforming data...")

    data = data.drop_duplicates()

    # optional cleaning
    data = data.dropna()

    print(f"✅ Transformed {len(data)} rows")
    return data


# -------------------
# LOAD
# -------------------
def load(data, table, ch_client):
    print("🔄 Loading to ClickHouse...")

    ch_client.insert_df(table, data)

    print("✅ Load complete")


# -------------------
# MAIN
# -------------------
if __name__ == "__main__":

    # MySQL connection
    mysql_engine = create_engine(
        "mysql+pymysql://school_user:school_password@localhost:3306/school_db"
    )

    # ClickHouse connection
    ch_client = clickhouse_connect.get_client(
        host='localhost',
        username='default',
        password='default',  # biasanya kosong
        database='school_db'
    )

    # ETL flow
    data = extract_data(
        engine=mysql_engine,
        query="SELECT * FROM students"
    )

    transformed_data = transform(data)

    load(transformed_data, 'students', ch_client)
