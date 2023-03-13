import sys

ac = len(sys.argv)

if ac == 3:
    if sys.argv[1].isdigit() == False:
        print(sys.argv[1], "is not an integer")
    elif sys.argv[2].isdigit() == False:
        print(sys.argv[2], "is not an integer")
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[2])

        print("Sum:", (a+b))
        print("Difference:", (a-b))
        print("Product:", (a*b))
        if b == 0:
            print("Quotient: ERROR (divison by zero)")
            print("Remainder: ERROR (modulo by zero)")
        else:
            print("Quotient:", (a/b))
            print("Remainder:", (a%b))
elif ac < 3:
    print("Usage: python3 operations.py <number1> <number2>")
    print("Example:")
    print(" python3 operations.py 10 3")
else:
    print("AssertionError: too many arguments")