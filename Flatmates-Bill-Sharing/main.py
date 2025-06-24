from bill import Bill
from flatmate import Flatmate
from pdf_report import PdfReport

from fpdf import FPDF

bill = Bill(amount=120 , period="April 2021")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)

print("John pays : ",john.pays(bill=bill,flatmate2=marry))
print("Marry pays : ",marry.pays(bill=bill,flatmate2=john))

report = PdfReport(filename="Report1.pdf")
report.generate(flatmate1=john,flatmate2=marry, bill=bill)