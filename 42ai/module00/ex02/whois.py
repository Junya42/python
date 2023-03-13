import sys

ac = len(sys.argv)
if ac != 2:
    print("One argument is required")
    exit(0)

if sys.argv[1].isdigit() == False:
    print("Argument is not only composed of digits")
    exit(0)

num = int(sys.argv[1])

print("Value " + sys.argv[1] + " is ", end="")
if num == 0:
    print("Zero")
elif num % 2:
    print("Odd")
else:
    print("Even")
