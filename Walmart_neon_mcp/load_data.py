import os
import sys
import psycopg2
from dotenv import load_dotenv

def load_data():
    load_dotenv(".env.local")
    db_url = os.getenv("DATABASE_URL_UNPOOLED") or os.getenv("DATABASE_URL")
    if not db_url:
        print("DATABASE_URL not found in .env.local", file=sys.stderr)
        sys.exit(1)

    print(f"Connecting to database...")
    conn = psycopg2.connect(db_url)
    cursor = conn.cursor()

    tables_files = [
        ("raw.stores", "walmart_dataset/data/stores.csv"),
        ("raw.customers", "walmart_dataset/data/customers.csv"),
        ("raw.products", "walmart_dataset/data/products.csv"),
        ("raw.employees", "walmart_dataset/data/employees.csv"),
        ("raw.orders", "walmart_dataset/data/orders.csv"),
        ("raw.order_items", "walmart_dataset/data/order_items.csv"),
    ]

    try:
        for table, file_path in tables_files:
            print(f"Loading {file_path} into {table} using copy_expert...")
            with open(file_path, "r", encoding="utf-8") as f:
                copy_sql = f"COPY {table} FROM STDIN WITH (FORMAT csv, HEADER true)"
                cursor.copy_expert(copy_sql, f)
            conn.commit()
            
            # Check row count
            cursor.execute(f"SELECT COUNT(*) FROM {table}")
            count = cursor.fetchone()[0]
            print(f"Successfully loaded {table}. Total rows: {count}")
    except Exception as e:
        conn.rollback()
        print(f"Error loading data: {e}", file=sys.stderr)
        cursor.close()
        conn.close()
        sys.exit(1)

    cursor.close()
    conn.close()
    print("All CSV data loaded successfully!")

if __name__ == "__main__":
    load_data()
