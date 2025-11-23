
import streamlit as st
st.set_page_config(page_title="CorpRFL-ACC Enterprise", layout="wide")

st.sidebar.title("CorpRFL-ACC Menu")
menu = st.sidebar.radio("Pilih Menu", [
    "Dashboard",
    "Perusahaan",
    "COA",
    "Jurnal",
    "General Ledger",
    "Trial Balance",
    "Balance Sheet",
    "Profit & Loss",
    "Export PDF",
    "Export Excel",
    "Invoice",
    "Upload Logo",
    "Backup & Restore"
])

st.write(f"# {menu}")
st.info("Routing final akan otomatis mengarah ke pages/ saat digabung ke repo utama.")
