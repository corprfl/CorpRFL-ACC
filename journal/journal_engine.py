
import sqlite3
from core.company_manager import get_active_company_db

def get_conn():
    return sqlite3.connect(get_active_company_db())

def list_journal():
    conn=get_conn(); cur=conn.cursor()
    cur.execute("SELECT * FROM journal ORDER BY date")
    rows=cur.fetchall()
    conn.close()
    return rows

def add_journal(date,voucher,account,account_name,desc_,ref,debit,credit,project):
    conn=get_conn(); cur=conn.cursor()
    cur.execute("""
        INSERT INTO journal (date,voucher,account,account_name,description,ref,debit,credit,project)
        VALUES (?,?,?,?,?,?,?,?,?)
    """,(date,voucher,account,account_name,desc_,ref,debit,credit,project))
    conn.commit(); conn.close()
