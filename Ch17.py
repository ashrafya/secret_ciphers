import random, time
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
myKey = 'QAZWSXEDCRFVTGBYHNUJIOPLKM'

def sub_cipher(string, key = myKey, mode = 'encrypt'):
    final=''
    if mode == 'encrypt':
        for character in string:
            upper = character.upper()
            if character not in LETTERS and upper in LETTERS:
                index = LETTERS.find(upper)
                final+=myKey[index].lower()
            elif character in LETTERS and upper in LETTERS:
                index = LETTERS.find(upper)
                final +=myKey[index]
            else:
                final+=character
    elif mode =='decrypt':
        for character in string:
            upper = character.upper()
            if character not in LETTERS and upper in LETTERS:
                index = myKey.find(upper)
                final+=LETTERS[index].lower()
            elif character in LETTERS and upper in LETTERS:
                index = myKey.find(upper)
                final +=LETTERS[index]
            else:
                final+=character            
    
    return final

def get_random_key():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key) 

def valid_key(key):
    if len(key) <len(LETTERS):
        return 'invalid key'
