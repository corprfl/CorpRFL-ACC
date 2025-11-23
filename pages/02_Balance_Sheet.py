
import streamlit as st
from modules.ledger_engine import balance_sheet
from core.company_manager import get_active_company

st.title("📘 Balance Sheet")

if not get_active_company():
    st.warning("Pilih perusahaan dulu.")
    st.stop()

df = balance_sheet()
st.dataframe(df, use_container_width=True)
