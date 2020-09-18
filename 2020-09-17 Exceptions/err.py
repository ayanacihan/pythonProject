#Error Handling
#b = "Hello"

#print(int(b)) #ValueError

while True: #this is new to us. While the user doesn't put a whole number, it will ask the same question again and again.
    try: #if the user doesn't put a whole number do this
        n = int(input("Please put a whole number:"))
        break
    except ValueError:
        print("No valid integer entered")
print("Great you have entered an integer") #if the user puts a whole number, print this