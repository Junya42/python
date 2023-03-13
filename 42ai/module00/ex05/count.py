import sys



'''
Cette function doit analyse la string(passez en argument avec arg) et compter le nombre de miniscule, majuscule, ponctuation et espace
'''
def text_analyzer(*argv):
    if len(argv) != 1:
        print("What is the text to analyze?")
    if argv[0].isdigit():
        print("Je veux un string")
    else:
        arg = argv[0]
        lower=0
        upper=0
        ponctuation=0
        espace=0
        total = 0
        for i in range(len(arg)):
            if arg[i].islower():
                lower+=1
            elif arg[i].isupper():
                upper+=1
            elif arg[i].isspace():
                espace+=1
            elif arg[i].isdigit() == False:
                ponctuation+=1
        total= lower+upper+ponctuation+espace
        return print("The text contains", total, "character(s):"+"\n"+"- ",upper," upper letter(s)\n" "- ",lower," lower letter(s)"+"\n"+"- ",ponctuation," punctation mark(s)"+"\n"+"- "+str(espace)+" space(s)"+"\n")