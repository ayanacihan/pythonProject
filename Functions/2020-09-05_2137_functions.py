#def sum(x,y):
#    print(x + y)

#sum(4,5)

def sum(x,y):
    return x + y

print(sum(4,5))
print(sum(8,4))

def student_names(names="Bluelime"):
    print("Hello " + names)

student_names()
student_names("John")
student_names("Jane")

def more_num(a,b=7,c=10):
    print("a is",a,"and b is",b,"while c is",c)

more_num(3,7)
more_num(23,c=17)
more_num(c=40,a=80)

def greeting():
    def say_hello():
        return "Hello"
    return say_hello
hello = greeting()

print(hello())

def mynum(x):
    return x + 1
num = mynum

print(num(7))
print(mynum(8))

x = 10

def my_numbers():
    global x
    print(x)
    x = 7
    print("My favorite number is", x)

my_numbers()

print(x)

def mynum(a):
    def num(a):
        return a + 1
    result = num(a)
    return result
print(mynum(4))

def display_message(message):
    "Hello"
    def message_sender():
        "Nested function"
        print(message)
    message_sender()
display_message("Show me the money!")

def dream_home():
    pass

def mynum(b):
    return b + 1
def addnum(c):
    newnum = 7
    return c(newnum)
print(addnum(mynum))

def total_numbers(a=7,*numbers,**phoneboook): #numbers will be tuple phonebook will be dictionary
    print("My fav number is", a)

    for num in numbers:
        print("num", num)

    for name, phone_number in phoneboook.items():
        print(name, phone_number)
total_numbers(7,1,2,3,Jane=2222,John=4444,Angela=5555)

a = lambda b: b + 4
print(a(4))

c = lambda d,e: d + e
print(c(7,8))

def ghost_number(n):
    return lambda f: f * n

double_num = ghost_number(2)

print(double_num(20))

def add_numbers(d,e):
    '''Adding two numbers

    The values must be integers'''
    print(d + e)

add_numbers(8,4)

print(add_numbers.__doc__)
