
import streamlit as st
from modules.ledger_engine import general_ledger
import pandas as pd
from core.company_manager import get_active_company

st.title("📘 General Ledger")

if not get_active_company():
    st.warning("Pilih perusahaan dulu.")
    st.stop()

df = general_ledger()
st.dataframe(df, use_container_width=True)
