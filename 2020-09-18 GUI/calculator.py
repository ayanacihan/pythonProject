#GUI interface
#for testing if it is really installed use this command
#python3 -m tkinter

from tkinter import *

class Application(Frame): #this will be the main class, Frame is used for grouping the widgets
#Main class for the calculator
    def _init_(self, master): #initialize the instance
#Initialize the Frame
        super(Application, self)._init_(master)    #returns a proxy object that delegates #master is parent widget
        self.task=""
        self.UserIn = StringVar()
        self.grid()
        self.create_widgets()

    def creat_widgets(self):
        self.user_input = Entry(self, bg = "#5BC8AC", bd = 29,
        insertwidth = 4, width = 24,
        font = ("Verdana", 20, "bold"), textvariable = self.UserIn, justify = RIGHT)
        self.user_input.grid(columnspan = 4)

        self.user_input.insert(0, "0")

        self.button7 = Button(self, bg = "#98DBC6", bd = 12,
        text = "7", padx = 33, pady = 25, font = ("Helvetica", 20, "bold"),
        command = lambda : self.buttonClick(7))
        self.button7.grid(row = 2, column = 0, sticky = W) #it will stretch the widget horizantally and vertically

        self.button8 = Button(self, bg = "#98DBC6", bd = 12,
        text = "8", padx = 33, pady = 25, font = ("Helvetica", 20, "bold"),
        command = lambda : self.buttonClick(8))
        self.button8.grid(row = 2, column = 0, sticky = W)

        self.button9 = Button(self, bg = "#98DBC6", bd = 12,
        text = "9", padx = 33, pady = 25, font = ("Helvetica", 20, "bold"),
        command = lambda : self.buttonClick(9))
        self.button9.grid(row = 2, column = 0, sticky = W)

        self.button4 = Button(self, bg = "#98DBC6", bd = 12,
        text = "4", padx = 33, pady = 25, font = ("Helvetica", 20, "bold"),
        command = lambda : self.buttonClick(4))
        self.button4.grid(row = 2, column = 0, sticky = W)

        self.button5 = Button(self, bg = "#98DBC6", bd = 12,
        text = "5", padx = 33, pady = 25, font = ("Helvetica", 20, "bold"),
        command = lambda : self.buttonClick(5))
        self.button5.grid(row = 2, column = 0, sticky = W)

        self.button6 = Button(self, bg = "#98DBC6", bd = 12,
        text = "6", padx = 33, pady = 25, font = ("Helvetica", 20, "bold"),
        command = lambda : self.buttonClick(6))
        self.button6.grid(row = 2, column = 0, sticky = W)

        self.button1 = Button(self, bg = "#98DBC6", bd = 12,
        text = "1", padx = 33, pady = 25, font = ("Helvetica", 20, "bold"),
        command = lambda : self.buttonClick(1))
        self.button1.grid(row = 2, column = 0, sticky = W)

        self.button2 = Button(self, bg = "#98DBC6", bd = 12,
        text = "2", padx = 33, pady = 25, font = ("Helvetica", 20, "bold"),
        command = lambda : self.buttonClick(2))
        self.button2.grid(row = 2, column = 0, sticky = W)

        self.button3 = Button(self, bg = "#98DBC6", bd = 12,
        text = "3", padx = 33, pady = 25, font = ("Helvetica", 20, "bold"),
        command = lambda : self.buttonClick(3))
        self.button3.grid(row = 2, column = 0, sticky = W)

    #there are more buttons above

    def buttonClick(self, number):
        self.task = str(self.task) + str(number)
        self.UserIn.set(self.task)

    def CalculateTask(self):
        self.data = self.user_input.get()
        try:
            self.answer = eval(self.data)
            self.displayText(self.answer)
            self.task = self.answer
        except SyntaxError as e:
            self.displayText("Invalid Syntax!")
            self.task = ""

    def displayText(self, value):
        self.user_input.delete(0, END)
        self.user_input.insert(0, value)

    def ClearDisplay(self):
        self.task = ""
        self.user_input.delete(0, END)
        self.user_input.insert(0, "0")

calculator = Tk()

calculator.title("Calculator")
app = Application(calculator)

calculator.resizable(width=False, height=False)

calculator.mainloop()