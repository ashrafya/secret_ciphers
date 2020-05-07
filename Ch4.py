import math
Letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def brute_force(message):
    #only takes in capital numbers, too long to allow all cases
    for key in range(len(Letters)):
        final=''
        for symbol in message:
            if symbol not in Letters:
                final+=symbol
            else:
                num = Letters.find(symbol)-key
                if num<0:
                    num+=len(Letters)
                final+=Letters[num]
        print("with key #%s : %s" %  (key, final))
        
x='frpprq vhqvh lv qrw vr frpprq.'

