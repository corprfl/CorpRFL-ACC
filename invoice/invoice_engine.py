
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm

def draw_header(c, company, logo_path=None):
    c.setFont("Helvetica-Bold", 15)
    c.drawString(20*mm, 280*mm, company)
    if logo_path:
        try:
            c.drawImage(logo_path, 160*mm, 265*mm, width=30*mm, height=30*mm)
        except:
            pass
    c.line(20*mm, 262*mm, 190*mm, 262*mm)

def draw_footer(c):
    c.setFont("Helvetica", 8)
    c.drawRightString(190*mm, 10*mm, "CorpRFL-ACC Invoice")

def export_invoice(filename, company, invoice_no, date, customer, items, logo_path=None):
    c = canvas.Canvas(filename, pagesize=A4)
    draw_header(c, company, logo_path)

    y = 250*mm
    c.setFont("Helvetica", 11)
    c.drawString(20*mm, y, f"Invoice No: {invoice_no}")
    y -= 6*mm
    c.drawString(20*mm, y, f"Date: {date}")
    y -= 6*mm
    c.drawString(20*mm, y, f"Billed To: {customer}")
    y -= 10*mm

    c.setFont("Helvetica-Bold", 10)
    c.drawString(20*mm, y, "Description")
    c.drawString(120*mm, y, "Amount")
    y -= 6*mm

    total = 0
    c.setFont("Helvetica", 10)
    for desc, amt in items:
        c.drawString(20*mm, y, str(desc))
        c.drawRightString(180*mm, y, f"{amt:,.2f}")
        total += amt
        y -= 6*mm
        if y < 20*mm:
            draw_footer(c)
            c.showPage()
            draw_header(c, company, logo_path)
            y = 250*mm

    y -= 10*mm
    c.setFont("Helvetica-Bold", 11)
    c.drawRightString(180*mm, y, f"Total: {total:,.2f}")

    draw_footer(c)
    c.save()
