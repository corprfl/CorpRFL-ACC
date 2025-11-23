
import sqlite3, os

def get_db_path(company):
    return f"companies/{company}.db"

def init_company_db(company):
    path = get_db_path(company)
    conn = sqlite3.connect(path)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT,
            name TEXT,
            type TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS journal (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            voucher TEXT,
            account TEXT,
            account_name TEXT,
            description TEXT,
            ref TEXT,
            debit REAL,
            credit REAL,
            project TEXT
        )
    """)

    conn.commit()
    conn.close()
