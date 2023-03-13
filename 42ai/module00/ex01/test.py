import sys
import dis

def func(argv):
    longueur = len(argv)
    if longueur == 0:
        exit()

    argument = ""
    for count in range(1, longueur):
            argument += argv[count]
            if count < longueur - 1:
                argument += " "
    print(argument[::-1].swapcase())

def main():
    dis.dis(func(sys.argv))
