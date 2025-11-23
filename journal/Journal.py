
import streamlit as st
from modules.journal_engine import add_journal, list_journal
from core.company_manager import get_active_company
import pandas as pd

st.title("📘 Journal Entry")

company = get_active_company()
if not company:
    st.warning("Pilih perusahaan dulu.")
    st.stop()

st.subheader("Tambah Jurnal Baru")
with st.form("journal_form"):
    date = st.date_input("Tanggal")
    voucher = st.text_input("No Voucher")
    account = st.text_input("Nomor Akun")
    account_name = st.text_input("Nama Akun")
    desc_ = st.text_input("Keterangan")
    ref = st.text_input("Ref")
    debit = st.number_input("Debit", min_value=0.0)
    credit = st.number_input("Credit", min_value=0.0)
    project = st.text_input("Project")
    save = st.form_submit_button("Simpan")
    if save:
        add_journal(str(date),voucher,account,account_name,desc_,ref,debit,credit,project)
        st.success("Jurnal disimpan!")

st.write("---")
st.subheader("Daftar Jurnal")
rows = list_journal()
df = pd.DataFrame(rows, columns=["ID","Tanggal","Voucher","Akun","Nama Akun","Keterangan","Ref","Debit","Credit","Project"])
st.dataframe(df, use_container_width=True)
