import pyperclip

alphabets = {'A':0,'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R': 17, 'S':18, 'T':19, 'U':20, \
             'V':21, 'W':22, 'X':23 , 'Y':24, 'Z':25}
opp = {0:'A',1:'B',2:'C', 3:'D', 4:'E', 5:'F', 6:'G', 7:'H', 8:'I', 9:'J', 10:'K',11:'L', 12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R', 18:'S', 19:'T', 20:'U', 21: 'V', \
       22:'W', 23:'X', 24:'Y', 25:'Z'}

    

            
        
def value_reverse_shift(letter, shift):
    letter = letter.upper()
    if letter not in alphabets:
        return letter
    if letter.upper() in alphabets:
        value = alphabets[letter]
        value-=shift
        while value<0:
            value+=26
        return opp[value]


def value_after_shift(letter, shift):
    letter = letter.upper()
    if letter not in alphabets:
        return letter
    
    if letter.upper() in alphabets:
        
        value = alphabets[letter]
        value += shift
        while value >=26:
            value -= 26
        return opp[value]


        

def decrypt_ceasar(string, shift):
    L=[]
    empty=''
    final=''
    for char in string:
        empty += value_reverse_shift(char, shift)
        case = check_case(char)
        L.append(case)
    for i in range(len(empty)):
        if L[i] == 'na' or L[i] == 1:
            final+=empty[i]
        else:
            final+=empty[i].lower()    
    return final  
    
    
def encrypt_caesar(string, shift):
    L=[]
    empty =''
    final=''
    for char in string:
        empty+=value_after_shift(char, shift)
        case = check_case(char)
        L.append(case)
    for i in range(len(empty)):
        if L[i] == 'na' or L[i] == 1:
            final+=empty[i]
        else:
            final+=empty[i].lower()
    
        
    return final
    
        

def check_case(letter):
    upper = letter.upper()
    if letter not in alphabets and upper not in alphabets:
        return 'na'
    elif letter == upper:
        return 1
    else:
        return 0


def what_shift(string, encrypted):
    for i in range(len(string)):
        upper = string[i].upper()
        upper_fk= encrypted[i].upper()
        if upper in alphabets:
            shift = alphabets[upper_fk] -alphabets[upper]
            if shift<0:
                shift+=26
            return shift
            
def find_set(key_list):
    i=0
    not_done = True
    tester=[]
    while not_done:
                
        if key_list[i] == None:
            return None
        if key_list[i] !=None:
            tester.append(key_list[i])
            i+=1
        if key_list[i] == None:
            return tester
        if key_list[i] !=None:
            tester.append(key_list[i])
            i+=1
        
        half = int(len(tester)/2)
            
        if tester[:half] == tester[half:]:
            return tester[:half]
        