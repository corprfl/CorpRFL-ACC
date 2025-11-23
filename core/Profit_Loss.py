
import streamlit as st
from modules.ledger_engine import profit_loss
from core.company_manager import get_active_company

st.title("📘 Profit & Loss")

if not get_active_company():
    st.warning("Pilih perusahaan dulu.")
    st.stop()

df = profit_loss()
st.dataframe(df, use_container_width=True)
