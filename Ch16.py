import Ch12, Ch15, Ch14

x = """yjcv"vjg"hwem"ku"iqkpi"qp"ykvj"eqtqtpc"kotcp"dtq"""

def hack_affine(string):
    print('hacking...\nPress ctrl+C to exit')
    #for i in range(1,len(Ch15.SYMBOLS) ** 2):
        #print(i)
    

    for i in range(1,len(Ch15.SYMBOLS) ** 2):
        key1= Ch15.get_key_parts(i)[0]
        if Ch14.gcd(key1, len(Ch15.SYMBOLS)) != 1 :
    
            continue
        decrypted = Ch15.affine_cipher(string, i, 'decrypt')        
        print('key #%s ... (%s)' %(i, decrypted))
        if Ch12.is_english(decrypted):
            print()
            print("possible key is %s\n\n" %i)
            print('decrypted message is %s' %decrypted[:100])
            print()
            d= input('want to keep going, yes or no')
            if d == 'yes':
                continue
            else:
                return 'DONE'
    
    return None, 'no key found'
          