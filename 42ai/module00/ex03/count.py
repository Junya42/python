import sys

def text_analyzer(str_arg=None):
    """ 
    This function takes a single string argument and displays
the sums of its upper-case characters, lower-case characters, punctuation characters and
spaces. """

    if str_arg is None:
        str_arg = input("What is the text to analyze ?\n")
    if type(str_arg) != str:
        print("AssertionError: Argument is not a string")
    else:
        up = 0
        low = 0
        punc = 0
        space = 0
        for i in str_arg:
            if i.isupper():
                up += 1
            elif i.islower():
                low += 1
            elif i.isspace():
                space += 1
            elif i.isdigit() == False:
                punc += 1
        total = up + low + space + punc
        print("The text contains", total, "character(s)")
        print("-", up , "upper letter(s)")
        print("-", low, "lower letter(s)")
        print("-", punc, "punctuation mark(s)")
        print("-", space, "space(s)")
        


size = len(sys.argv)

if size == 2:
    var = sys.argv[1]
    text_analyzer(var)
elif size > 2:
    print("Send one agument only")