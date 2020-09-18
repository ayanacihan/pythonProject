#c = 12/0 #ZeroDivisionError

#print(x) #NameError

#print(int("hi")) #ValueError

try:
    n = 12/ int(input("Enter a whole number:"))
    print("The value of your number is:", n)
except ZeroDivisionError as e: #it brings what python brings as error statement default.
    print(e)
except ValueError as e: #it brings what python brings as error statement default.
    print(e)

finally:
    print("Hope you entered a valid whole number")