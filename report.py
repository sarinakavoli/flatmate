import webbrowser
import os

from fpdf import FPDF


class PdfReport:
    """
    Creates a pdf file that contains data about the flatmates such as
    their names, their due amount and the period od the bill.
    """
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='p', unit='pt', format="A4")
        pdf.add_page()

        #Add image
        pdf.image("files/house.png", w=30, h=30)
        # ADD the title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=200, h=80, txt="Flatmates Bill", border=1, align="C", ln=1)

        #Insert period label and value
        pdf.set_font(family="Times", size=14, style="B")
        pdf.cell(w=100, h=40, txt="Period", border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family ="Times", size=12)
        pdf.cell(w=100, h=40, txt= flatmate1.name, border=1)
        pdf.cell(w=150, h=40, txt=flatmate1_pay, border=1, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=150, h=40, txt=flatmate2_pay, border=1, ln=1)

        #It will change directory to files, generate and open pdf.
        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)
