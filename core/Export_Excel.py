
import streamlit as st
from core.company_manager import get_active_company
from modules.ledger_engine import general_ledger, trial_balance, balance_sheet, profit_loss
from export.excel_engine import export_excel
import pandas as pd

st.title("📊 Export Excel")

company = get_active_company()
if not company:
    st.warning("Pilih perusahaan dulu.")
    st.stop()

if st.button("Export General Ledger Excel"):
    df = general_ledger()
    export_excel(df, "gl.xlsx")
    with open("gl.xlsx","rb") as f:
        st.download_button("Download GL.xlsx", f, "GL.xlsx")

if st.button("Export Trial Balance Excel"):
    df = trial_balance()
    export_excel(df, "tb.xlsx")
    with open("tb.xlsx","rb") as f:
        st.download_button("Download TB.xlsx", f, "TB.xlsx")

if st.button("Export Balance Sheet Excel"):
    df = balance_sheet()
    export_excel(df, "bs.xlsx")
    with open("bs.xlsx","rb") as f:
        st.download_button("Download BS.xlsx", f, "BS.xlsx")

if st.button("Export Profit & Loss Excel"):
    df = profit_loss()
    export_excel(df, "pl.xlsx")
    with open("pl.xlsx","rb") as f:
        st.download_button("Download PL.xlsx", f, "PL.xlsx")
