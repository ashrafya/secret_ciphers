import Ch12, Ch9

def hack_transposition(string):
    print("hacking...\nPress ctrl+C to quit at any time")
    going = True
    while going:    
    
        for key in range(1,len(string)):
            
            print("Trying key #%s\n\n" %key)
                
            decrypted = Ch9.decrypt_transformation_cipher(string, key)
                
            result = Ch12.is_english(decrypted)
            if result ==1:
                print('possible key is %s' %key)
                print(decrypted.upper())
            else:
                print('%s is not a possible key' %key)
                
                    
            keep_on = input("press Y or N if you want to keep hacking    ")
            if keep_on == 'y' or keep_on == 'Y':
                going = True
            if keep_on == 'n' or keep_on == "N":
                going = False
                return None
                
    return None
                
             