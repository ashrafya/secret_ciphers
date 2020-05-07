import math
def decrypt_transformation_cipher(string, key):
    '''
    has minor errors
    '''
    L=[]
    point=0
    within=True
    count=0
    
    columns=math.ceil(len(string)/key)
    maxim=key*columns
    numOfRows=key
    
    remainder=maxim-len(string)
    row=1 #to deal with the empty box shift 
    i=1
    
    while within:
        #L.append(string[count])
        #count+=1
        #if count >=len(string)-1:
            #within=False
        
        if point>=len(string):
            point=0
            count+=1
            point=count
            i=1
            row=1
            
        if row>(key-remainder)+1:
            L.append(string[point-i])
            i+=1
        else:  
            L.append(string[point])
        
        if len(L)>=len(string) or point>len(string):
            within = False
            
        point+=columns
        row+=1
        
        
    return ''.join(L)


x='cenoonommstmme oo snnio s s c'
