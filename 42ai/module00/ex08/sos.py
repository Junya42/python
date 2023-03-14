import sys

morse_base = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ' ': '/',
}

def encode(data):
    #split_data = [letters for letters in data]
    #split_data = split_data.upper()
    split_data = data.upper()
    new_data = ""
    for letter in range(0, len(split_data)):
        if split_data[letter] in morse_base.keys():
            new_data += morse_base[split_data[letter]]
            if letter < len(split_data) - 1:
                new_data += ' '
        else:
            print("Invalid characters found in provided argument(s)")
            return
    print(new_data)

size = len(sys.argv)
if size == 1:
    print("Error no arguments provided")
else:
    data = ""
    for i in range(1, size):
        data += sys.argv[i]
        if i < size - 1:
            data += ' '
    encode(data)