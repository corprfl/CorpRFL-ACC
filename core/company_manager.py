
import streamlit as st
import os

def load_companies():
    os.makedirs("companies", exist_ok=True)
    files = os.listdir("companies")
    companies = [f.replace(".db","") for f in files if f.endswith(".db")]
    return companies

def select_company(companies):
    add = st.sidebar.text_input("Tambah Perusahaan Baru")
    if st.sidebar.button("Tambah"):
        if add.strip():
            open(f"companies/{add}.db","w").close()
            st.sidebar.success("Perusahaan ditambahkan!")
    return st.sidebar.selectbox("Pilih Perusahaan", companies)
