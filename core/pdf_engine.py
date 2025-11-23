
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

def draw_header(c, title, company):
    c.setFont("Helvetica-Bold", 14)
    c.drawString(20*mm, 280*mm, company)
    c.setFont("Helvetica", 12)
    c.drawString(20*mm, 270*mm, title)
    c.line(20*mm, 268*mm, 190*mm, 268*mm)

def draw_footer(c):
    c.setFont("Helvetica", 8)
    c.drawRightString(190*mm, 10*mm, "CorpRFL-ACC Enterprise")

def export_simple_table(filename, title, company, rows, columns):
    c = canvas.Canvas(filename, pagesize=A4)
    draw_header(c, title, company)

    y = 260*mm
    c.setFont("Helvetica", 9)
    header = " | ".join(columns)
    c.drawString(20*mm, y, header)
    y -= 8*mm

    for r in rows:
        line = " | ".join([str(x) for x in r])
        c.drawString(20*mm, y, line)
        y -= 6*mm
        if y < 20*mm:
            draw_footer(c)
            c.showPage()
            draw_header(c, title, company)
            y = 260*mm

    draw_footer(c)
    c.save()
