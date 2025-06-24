from bill import Bill

class Flatmate:
    """
    Creates a flatmate person who lives in the flat and pays a share of the bill
    """
    def __init__(self, name:str, days_in_house:int):
        self.name = name 
        self.days_in_house = days_in_house
    
    def pays(self, bill:Bill, flatmate2):
        weight = float(self.days_in_house)/(float(self.days_in_house)+float(flatmate2.days_in_house))
        return bill.amount * weight