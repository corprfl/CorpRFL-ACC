
import streamlit as st
from core.company_manager import load_companies, select_company
from core.database import init_company_db

st.set_page_config(page_title="CorpRFL-ACC Enterprise", layout="wide")

st.title("📘 CorpRFL-ACC Enterprise")
st.caption("Batch 1: Core Engine")

st.sidebar.header("Company")

companies = load_companies()
company = select_company(companies)

if company:
    init_company_db(company)
    st.success(f"Perusahaan aktif: {company}")
else:
    st.info("Belum ada perusahaan. Tambahkan dari sidebar.")
