import sys, random, Ch14

SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\] ^_`abcdefghijklmnopqrstuvwxyz{|}~""" 

def check_keys(key1, key2, mode = 'encrypt'):
    if key1 == 1 and mode == 'encrypt':
        print('The affine cipher becomes incredibly weak when key A is set to 1. Choose a different key.')
        return 0
    if key2 == 0 and mode == 'encrypt':
        print('The affine cipher becomes incredibly weak when key B is set to 0. Choose a different key.')
        return 0
    if key1 < 0 or key2 < 0 or key2 > len(SYMBOLS) - 1:
        print('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(SYMBOLS) - 1))
        return 0
    if Ch14.gcd(key1, len(SYMBOLS)) != 1:
        print('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (key1, len(SYMBOLS)))
        return 0
        
def get_key_parts(key):
    key1 = key//len(SYMBOLS)
    key2 = key%len(SYMBOLS)
    return key1, key2

def random_keys():
    going= True
    while going:
        key1 = random.randint(2, len(SYMBOLS))
        key2 = random.randint(2, len(SYMBOLS))
        if Ch14.gcd(key1, len(SYMBOLS)) ==1:
            going = False
            return key1*len(SYMBOLS)+key2
        
def affine_cipher(string, key, mode ='encrypt'):
    reverse = True
    key1, key2 = get_key_parts(key)
    check_keys(key1, key2, 'encrypt')
    mod_inverse_key1 = Ch14.find_mod_inverse(key1, len(SYMBOLS))
    final=''
    
    #if Ch14.gcd(key1, key2) != 1:
        #reverse = False
        #print('this key cannot be decrypted')
        #sys.exit()
    if mode == 'encrypt' or mode == 'ENCRYPT':
        for symbol in string:
            if symbol in SYMBOLS:
                index = SYMBOLS.find(symbol)
                final+= SYMBOLS[(index*key1+key2)%len(SYMBOLS)]
            else:
                final+=symbol
    elif mode =='decrypt' or mode == 'DECRYPT':            
        for symbol in string:
            if symbol in SYMBOLS:
                index=SYMBOLS.find(symbol)
                final+= SYMBOLS[(index-key2) * mod_inverse_key1 % len(SYMBOLS)]
            else:
                final+=symbol
    return final
        
        
    
        
        
s=3081