import random
import string

def atoi(str):
    resultant = 0
    current = 0
    sign = 1
    while str[current]:
        if str[current] == '-' or str[current] == '+':
            if str[current] == '-':
                sign = -sign
            current += 1
        elif str[current].isdigit():
            break
        else:
            return current
    for i in range(current, len(str)):
        resultant = resultant * 10 + (ord(str[i]) - ord('0'))        #It is ASCII substraction 
    return resultant * sign

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")
print()

value = random.randint(1, 99)
tries = 0

while True:
    user = input("What's your guess between 1 and 99?\n>> ")
    user_int = atoi(user)
    print(user_int)
    if user_int != 0:
        if user_int > 99:
            print("Your number must not exceed 99")
        elif user_int < 0:
            print("Your number must be greater than 0")
        elif user_int > value:
            print("Too high!")
            tries += 1
        elif user_int < value:
            print("Too low!")
            tries += 1
        else:
            if value == 42:
                print("The answer to the ultimate question of lie, the universe and everything is 42.")
            if tries != 0:
                print("Congratulations, you've got it!")
                tries +=1
                print(f"You won in {tries} attempts!")
            else:
                print("Congratulations! You got it on your first try!")
            break
    elif user == "exit":
        break
    else:
        print("Value was incorrect or equal to 0")

print("Exiting guess.py")