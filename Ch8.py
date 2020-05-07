import math

def encrypt_transposition_cipher(string, key):
    '''
    encrypting with the transposition cipher
    '''
        
    point=0
    column = True
    count=0
    L=[]
    while column:
        L.append(string[point])
        point+=key
        
        if point>len(string)-1:
            count+=1
            point=count
        if len(L)>=len(string):
            column = False
    return ''.join(L)