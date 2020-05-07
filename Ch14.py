import Ch1_A

letters = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertuiopasdfghjklzxcvbnm'

OG ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

alphabets = {'A':0,'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R': 17, 'S':18, 'T':19, 'U':20, \
             'V':21, 'W':22, 'X':23 , 'Y':24, 'Z':25}

opp = {0:'A',1:'B',2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K',11:'L', 12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21: 'V', \
       22:'W', 23:'X', 24:'Y', 25:'Z'}


def gcd(a,b):
    while a!=0:
        a , b = b % a, a
    return b

def multiplication_cipher(string, key, mode = 'encrypt'):
    final =[]
    if mode == 'encrypt' or mode == 'ENCRYPT':
        for character in string:
            case = Ch1_A.check_case(character)
            if case =='na':
                final.append(character)
                continue
            upper = character.upper()
            number = alphabets[upper]
            number *=key
            number = number%len(opp)
            letter = opp[number]
            if case == 1:
                final.append(letter.upper())
                continue
            elif case == 0:
                final.append(letter.lower())
    elif mode == 'decrypt' or mode == 'DECRYPT':
        for character in string:
            case = Ch1_A.check_case(character)
            if case == 'na':
                final.append(character)
                continue
            upper = character.upper()
            
            for character in OG:
                x = multiplication_cipher(character, key)
                if x == upper:
                    if case == 1:
                        final.append(character.upper())
                    if case ==0:
                        final.append(character.lower())
                    break

            
                    
    return ''.join(final)

def find_mod_inverse(a,m):
    if gcd(a, m) != 1:
        return None # no mod inverse if a & m aren't relatively prime

    # Calculate using the Extended Euclidean Algorithm:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m