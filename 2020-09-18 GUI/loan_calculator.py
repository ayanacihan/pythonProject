from tkinter import * #importing everything. you can import certain parts or everything

class LoanCalculator:#properties and methods (functions). object constructor.
    def __init__(self): #can be used to assign values object properties. every time initiated when class is created.
#self is a variable that represents the instance of object itself
        window = Tk()
        window.title("Loan Calculator") #app window title
        window.configure(background = "light green")

        Label(window, font = "Helvetica 12 bold", bg = "light green", text = "Annual Interest Rate").grid(row = 1, column = 1, sticky = W) #table structure.
        Label(window, font = "Helvetica 12 bold", bg = "light green", text = "Number of Years").grid(row = 2, column = 1, sticky = W)
        Label(window, font = "Helvetica 12 bold", bg = "light green", text = "Loan Amount").grid(row = 3, column = 1, sticky = W)
        Label(window, font = "Helvetica 12 bold", bg = "light green", text = "Monthly Payment").grid(row = 4, column = 1, sticky = W)
        Label(window, font = "Helvetica 12 bold", bg = "light green", text = "Total Payment").grid(row = 5, column = 1, sticky = W)

        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable = self.annualInterestRateVar, justify = RIGHT).grid(row = 1, column = 2) #user enters some info here.

        self.numberofYearsVar = StringVar()
        Entry(window, textvariable = self.numberofYearsVar, justify=RIGHT).grid(row=2, column=2)

        self.loanAmountVar = StringVar()
        Entry(window, textvariable = self.loanAmountVar, justify=RIGHT).grid(row=3, column=2)

        self.monthlyPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, font = "Helvetica 12 bold", bg = "light green", textvariable = self.monthlyPaymentVar).grid(row = 4, column = 2, sticky = E)
        self.totalPaymentVar = StringVar()
        lblMonthlyPayment = Label(window, font = "Helvetica 12 bold", bg = "light green", textvariable = self.totalPaymentVar).grid(row = 5, column = 2, sticky = E)

        btComputePayment = Button(window, text = "Compute Payment", bg = "red", fg = "white", font = "Helvetica 14 bold", command = self.computePayment).grid(row = 6, column = 2, sticky = E)
        btClear = Button(window, text = "Clear", bg = "blue", fg = "white", font = "Helvetica 14 bold", command = self.delete_all).grid(row = 6, column = 8, padx = 20, pady = 20, sticky = E)

        window.mainloop()

    def computePayment(self):#be careful with the indentation. #method is also a function. Function in class is called method
        monthlyPayment = self.getMonthlyPayment(
            float(self.loanAmountVar.get()), #float: any number that can also include decimal numbers
            float(self.annualInterestRateVar.get())  / 1200,
            int(self.numberofYearsVar.get())) #int: whole number

        self.monthlyPaymentVar.set(format(monthlyPayment, '10.2f'))
        totalPayment = float(self.monthlyPaymentVar.get())  * 12 \
        * int(self.numberofYearsVar.get())

        self.totalPaymentVar.set(format(totalPayment, '10.2f'))

    def getMonthlyPayment(self, loanAmountVar, monthlyInterestRate, numberofYears):
        monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1 / (1 + monthlyInterestRate) ** (numberofYears * 12))
        return monthlyPayment

    def delete_all(self):
        self.monthlyPaymentVar.set("")
        self.loanAmountVar.set("")
        self.annualInterestRateVar.set("")
        self.numberofYearsVar.set("")
        self.totalPaymentVar.set("")

LoanCalculator()