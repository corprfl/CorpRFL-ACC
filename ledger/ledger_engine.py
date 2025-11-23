
import sqlite3
import pandas as pd
from core.company_manager import get_active_company_db

def get_conn():
    return sqlite3.connect(get_active_company_db())

def get_journal_df():
    conn=get_conn()
    df=pd.read_sql_query("SELECT * FROM journal ORDER BY date", conn)
    conn.close()
    return df

def general_ledger():
    df=get_journal_df()
    if df.empty: return df
    df['Balance']=df['debit']-df['credit']
    return df

def trial_balance():
    df=get_journal_df()
    if df.empty: return df
    tb=df.groupby('account').agg({'debit':'sum','credit':'sum'}).reset_index()
    tb['Balance']=tb['debit']-tb['credit']
    return tb

def balance_sheet():
    df=trial_balance()
    if df.empty: return df
    df['type']=df['account'].apply(lambda x: 
        "Asset" if str(x).startswith("1") else 
        "Liability" if str(x).startswith("2") else
        "Equity" if str(x).startswith("3") else "")
    return df[df['type'].isin(["Asset","Liability","Equity"])]

def profit_loss():
    df=trial_balance()
    if df.empty: return df
    df['type']=df['account'].apply(lambda x:
        "Revenue" if str(x).startswith("4") else
        "Expense" if str(x).startswith("5") else "")
    return df[df['type'].isin(["Revenue","Expense"])]
