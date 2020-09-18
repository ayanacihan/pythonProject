import random

guesses = [] #array
myComputer = random.randint(1,100)
player = int(input("Please guess the number of the computer. Between 1-100. Let's start! "))
guesses.append(player) #every guess will be added to the array

while myComputer != player:
    if player > myComputer:
        print("Number is too high")
    else:
        print("Number is too low")
    player = int(input("Enter a number between 1-100 "))
    guesses.append(player)

else:
    print("You have guessed right Good job")
    print("It took you %i guesses" %len(guesses))
    print(guesses)