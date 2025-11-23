
import sqlite3
from core.company_manager import get_active_company_db

def get_conn():
    return sqlite3.connect(get_active_company_db())

def list_accounts():
    conn=get_conn(); cur=conn.cursor()
    cur.execute("SELECT id, code, name, type FROM accounts ORDER BY code")
    rows=cur.fetchall()
    conn.close()
    return rows

def add_account(code, name, type_):
    conn=get_conn(); cur=conn.cursor()
    cur.execute("INSERT INTO accounts (code,name,type) VALUES (?,?,?)",(code,name,type_))
    conn.commit(); conn.close()

def delete_account(acc_id):
    conn=get_conn(); cur=conn.cursor()
    cur.execute("DELETE FROM accounts WHERE id=?",(acc_id,))
    conn.commit(); conn.close()
