#Answer 5
class Expenditure:
    ''' class to add and calculate expenditure'''

    def __init__(self):
        self.salary=200000
        self.savings=50000
        self.category='a'
        self.totalexp=20000

    def AddExpenditure(self):
        if self.category=='a':
            self.expenditure=36000
        elif self.category=='b':
            self.expenditure=30000.0

    def CalcTotalExp(self):
        self.totalexp+=self.expenditure

    def CalcPerDayAndMonthlyExp(self):
        self.perDayExp=self.totalexp/365
        self.monthlyExp=self.totalexp/12


    def Display(self):
        print("Salary",self.salary)
        print("Savings",self.savings)
        print("Category",self.category)
        print("Expenditure",self.expenditure)
        print("Total Expenditure",self.totalexp)
        print("Per Month Expenditure",self.monthlyExp)
        print("Daily Expenditure",self.perDayExp)

e=Expenditure()
e.AddExpenditure()
e.CalcTotalExp()
e.CalcPerDayAndMonthlyExp()
e.Display()
