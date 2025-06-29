from bill import Bill
from flatmate import Flatmate
from pdf_report import PdfReport

amount = float(input("Hey user enter the bill amount : "))
period = input("What is the Bill period (Eg December 2020): ")

name1 = input("What is your name ? ")
daysInHouse1 = int(input(f"How many days did {name1} stay in house ? "))


name2 = input("What is your name of other flatmate : ")
daysInHouse2 = int(input(f"How many days did {name2} stay in house ? "))

bill = Bill(amount, period)
flatmate1 = Flatmate(name1, daysInHouse1)
flatmate2 = Flatmate(name2, daysInHouse2)

print(f"{flatmate1.name} pays : ",flatmate1.pays(bill=bill,flatmate2=flatmate2))
print(f"{flatmate2.name} pays : ",flatmate2.pays(bill=bill,flatmate2=flatmate1))

report = PdfReport(filename=f"{bill.period}.pdf")
report.generate(flatmate1,flatmate2, bill=bill)