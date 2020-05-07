import Ch9, Ch8, math
import time

def encrypt_transposition_file(filename, key):
    input_f=open(filename + '.txt', 'r')    
    output = open(filename+'_encrypted.txt', 'w')
    tic = time.time()
    
    output.write(str(Ch8.encrypt_transposition_cipher(input_f.read(), key)))
    toc = time.time()
    
    output.close()
    input_f.close()
    print("it took %s seconds" %round((toc-tic),3),'\n')
    
    
    
    

def decrypt_transposition_file(filename, key):
    input_f=open(filename + '.txt', 'r')
    output = open(filename + '_decrypted.txt', 'w')
    
    
    tic = time.time()
    
    output.write(str(Ch9.decrypt_transformation_cipher(input_f.read(), key)))
    toc = time.time()
    
    
    output.close()
    input_f.close()    
    print("it took %s seconds" %round((toc-tic),3),'\n')
    
    
    
    
    
    
def check_work(string,key):
    encrypt = book_encrypt_trans(string, key)
    
    decrypt = book_decrypt_trans(encrypt,key)
    my_decrypt = Ch9.decrypt_transformation_cipher(encrypt,key)
    if decrypt == my_decrypt:
        print(string,'\n', decrypt, '\n',my_decrypt)
        return 'fucking works'
    else:
        print(string,'\n',my_decrypt,'\n',decrypt)
        return my_decrypt == decrypt
