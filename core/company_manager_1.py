
import streamlit as st
import os

active_company = None

def get_active_company():
    return active_company

def get_active_company_db():
    if active_company:
        return f"companies/{active_company}.db"
    return None

def load_companies():
    os.makedirs("companies", exist_ok=True)
    files = os.listdir("companies")
    companies = [f.replace(".db","") for f in files if f.endswith(".db")]
    return companies

def select_company(companies):
    global active_company
    add = st.sidebar.text_input("Tambah Perusahaan Baru")
    if st.sidebar.button("Tambah"):
        if add.strip():
            open(f"companies/{add}.db","w").close()
            st.sidebar.success("Perusahaan ditambahkan!")
    active_company = st.sidebar.selectbox("Pilih Perusahaan", companies)
    return active_company
