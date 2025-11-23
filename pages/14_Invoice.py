
import streamlit as st
from export.invoice_engine import export_invoice
from core.company_manager import get_active_company
import os

st.title("🧾 Invoice Generator")

company = get_active_company()
if not company:
    st.warning("Pilih perusahaan dulu.")
    st.stop()

invoice_no = st.text_input("Invoice No")
date = st.date_input("Tanggal")
customer = st.text_input("Customer")

st.subheader("Items")
items = []
count = st.number_input("Jumlah Item", min_value=1, value=1)
for i in range(count):
    desc = st.text_input(f"Deskripsi {i+1}")
    amt = st.number_input(f"Amount {i+1}", min_value=0.0)
    items.append((desc, amt))

logo_path = None
logo_file = f"companies/{company}/logo.png"
if os.path.exists(logo_file):
    logo_path = logo_file
    st.info("Logo perusahaan terdeteksi dan akan digunakan.")

if st.button("Generate Invoice PDF"):
    export_invoice("invoice.pdf", company, invoice_no, str(date), customer, items, logo_path)
    with open("invoice.pdf","rb") as f:
        st.download_button("Download Invoice.pdf", f, "Invoice.pdf")
