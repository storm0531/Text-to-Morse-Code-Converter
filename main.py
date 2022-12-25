MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}
## can use a reversed dictionary from MORSE_CODE_DICT to decode code_text
# def reverse_dict(DICT):
#     reversed = {}
#     for key,value in DICT.items():
#         reversed[value] = key
#     return reversed
# print(reverse_dict(MORSE_CODE_DICT))

##or reverse with dict comprehension
# reversed =  { values : keys for keys ,values in MORSE_CODE_DICT.items()}
# print(reversed)

def encrypt(plain_text):
    morse_code = ""
    for letter in plain_text:
        if letter == " ":
            morse_code += " "
        else:
            morse_code += MORSE_CODE_DICT[letter.upper()] + " "
    return morse_code


def decrypt(encrypted_text):
    text = ""
    for code in encrypted_text.split(" "):
        if code == "":
            text += " "
        else:
            for i in MORSE_CODE_DICT:
                if MORSE_CODE_DICT[i] == code:
                    text += i
    return text


again = True
while again:
    code_process = input("for encrypt put:en ,for decrypt put:de\n")
    user_text = input("Write the text that wanting to convert:\n")
    print(user_text)
    if code_process == "de":
        print(f"your text has been encoded:\n{decrypt(user_text)}")
    else:
        print(f"your code has been decoded:\n{encrypt(user_text)}")

    continue_again = input("are you wish to use this tools again? y,n?")
    if continue_again == "n":
        again = False
