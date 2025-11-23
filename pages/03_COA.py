
import streamlit as st
from modules.coa_engine import list_accounts, add_account, delete_account
from core.company_manager import get_active_company

st.title("📒 Chart of Accounts")

company = get_active_company()
if not company:
    st.warning("Pilih perusahaan dulu.")
    st.stop()

st.subheader("Tambah Akun Baru")
with st.form("coa_form"):
    code = st.text_input("Kode Akun")
    name = st.text_input("Nama Akun")
    type_ = st.selectbox("Tipe", ["Asset","Liability","Equity","Revenue","Expense"])
    submit = st.form_submit_button("Simpan")
    if submit:
        add_account(code,name,type_)
        st.success("Akun ditambah!")

st.write("---")
st.subheader("Daftar Akun")

rows = list_accounts()
for r in rows:
    st.write(f"{r[1]} - {r[2]} ({r[3]})")
    if st.button(f"Hapus {r[0]}", key=r[0]):
        delete_account(r[0])
        st.experimental_rerun()
