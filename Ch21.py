import Ch19, Ch12, time


def main():
    ciphertext = 'Lazn ifxrc xpslxj '

    hacked = hack_dict_vignere(ciphertext)
    
    if hacked == None:
        print('failed to hack')
    else:
        print('hacked message is %s' %str(hacked))

def hack_dict_vignere(string):
    f = open('dictionary.txt','r')
    lists = f.readlines()
    f.close()
    print('hacking...')
    tic = time.time()
    
    for word in lists:
        word = word.strip()
        decrypted= Ch19.vignere(string, word, mode = 'decrypt')
        if Ch12.is_english(decrypted, wordPercentage=50):
            toc = time.time()
            print()
            print('possible encryption break is')
            print('key %s : decrypted[:30] = %s ' %(str(word.upper()) ,str(decrypted[:30])))
            print()
            print('took %s seconds to hack' %round(toc-tic,3))
            print()
            x = input('want to keep going, yes or no')
            if x=='no':
                return decrypted
        
        


if __name__ == '__main__':
    main()