
import streamlit as st
import pandas as pd
from export.pdf_engine import export_simple_table
from core.company_manager import get_active_company
from modules.ledger_engine import general_ledger, trial_balance, balance_sheet, profit_loss

st.title("📄 Export PDF")

company = get_active_company()
if not company:
    st.warning("Pilih perusahaan dulu.")
    st.stop()

st.subheader("General Ledger PDF")
if st.button("Generate GL PDF"):
    df = general_ledger()
    export_simple_table("gl.pdf", "General Ledger", company, df.values.tolist(), df.columns.tolist())
    with open("gl.pdf","rb") as f:
        st.download_button("Download GL.pdf", f, file_name="GL.pdf")

st.subheader("Trial Balance PDF")
if st.button("Generate TB PDF"):
    df = trial_balance()
    export_simple_table("tb.pdf", "Trial Balance", company, df.values.tolist(), df.columns.tolist())
    with open("tb.pdf","rb") as f:
        st.download_button("Download TB.pdf", f, file_name="TB.pdf")

st.subheader("Balance Sheet PDF")
if st.button("Generate BS PDF"):
    df = balance_sheet()
    export_simple_table("bs.pdf", "Balance Sheet", company, df.values.tolist(), df.columns.tolist())
    with open("bs.pdf","rb") as f:
        st.download_button("Download BS.pdf", f, file_name="BS.pdf")

st.subheader("Profit & Loss PDF")
if st.button("Generate PL PDF"):
    df = profit_loss()
    export_simple_table("pl.pdf", "Profit & Loss", company, df.values.tolist(), df.columns.tolist())
    with open("pl.pdf","rb") as f:
        st.download_button("Download PL.pdf", f, file_name="PL.pdf")
