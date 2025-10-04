import psycopg2
from config import config_db
from psycopg2.extras import execute_batch


def get_connection():
    return psycopg2.connect(
        host=config_db["HOST"],
        port=config_db["PORT"],
        user=config_db["USER"],
        password=config_db["PASSWORD"],
        dbname=config_db["DATABASE"],
    )

def insert_rows(rows):
    if not rows:
        return
    
    conn = get_connection()
    cur = conn.cursor()

    colonnes = ", ".join(rows[0].keys())
    placeholders = ", ".join(["%s"] * len(rows[0]))
    
    query = f"INSERT INTO raw_dvf ({colonnes}) VALUES ({placeholders})"
    
    data = [tuple(row.values()) for row in rows]
    
    execute_batch(cur, query, data, page_size=1000)
    
    conn.commit()
    cur.close()
    conn.close()


