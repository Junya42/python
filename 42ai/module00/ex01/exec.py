import sys

i = 0
stock_arguments = ""
for banane in sys.argv:
    if i != 0:
        if len(stock_arguments) > 0:
            stock_arguments += " "
        stock_arguments += banane
    i = i + 1

stock_arguments = stock_arguments[::-1]
stock_arguments = stock_arguments.swapcase()
print(stock_arguments)
