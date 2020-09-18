#This is one example of an exception. dividing the number with 0
'''6/0
Traceback (most recent call last):
  File "<input>", line 1, in <module>
ZeroDivisionError: division by zero'''

#Handling Exceptions
#try: test a block of code for errors
#except: how to handle the errors
#finally: what code to execute regardless of what happens in try except block
#else: if no exception the code runs inside of else block.

#NameErrors

#print(x) #Normally only this code gives error. It doesn't have specified variable.
x = 20
try:
    print(x)
except:
    print("Variable is not defined")
else:
    print("Hello") #if no error occures it prints Hello
finally:
    print("You may get error if no variable is specified") #