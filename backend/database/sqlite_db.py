import sqlite3


def get_connection():
    return sqlite3.connect("data/claims.db") 


def create_claims_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS claims (
        claim_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name  TEXT,
        customer_email  TEXT,
        policy_number  TEXT,
        claim_type   TEXT,
        claim_amount  REAL,
        incident_date  TEXT,
        incident_location TEXT,
        incident_description  TEXT,
        status  TEXT,
        created_at TEXT
        )
    """)

    conn.commit()
    conn.close()