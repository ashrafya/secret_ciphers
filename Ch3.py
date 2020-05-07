def reverse_cipher(string):
    final=''
    index = len(string)-1
    while index>=0:
        final+=string[index]
        index-=1
    return final