import sys
import string

size = len(sys.argv)

if size != 3:
    print("Usage: python3 filterwords.py <string> <number>")
elif sys.argv[2].isdigit() == False:
    print("Argument two needs to be a number")
else:
    min_size = int(sys.argv[2])
    words = sys.argv[1].split()
    new_list = []
    for word in words:
        for i in range(0, len(word)):
            if word[i] in string.punctuation:
                for p in string.punctuation:
                    word = word.replace(p, '')
        if len(word) > min_size:
            new_list.append(word)
    print(new_list)