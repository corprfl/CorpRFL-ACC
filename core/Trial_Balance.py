
import streamlit as st
from modules.ledger_engine import trial_balance
from core.company_manager import get_active_company

st.title("📘 Trial Balance")

if not get_active_company():
    st.warning("Pilih perusahaan dulu.")
    st.stop()

df = trial_balance()
st.dataframe(df, use_container_width=True)
