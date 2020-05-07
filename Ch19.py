letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def vignere(string, key, mode = 'encrypt'):
    
    SET = []
    final=''
    
    for character in key:
        character = character.upper()
        SET.append(letters.find(character))
    
        
    count=0
    if mode =='encrypt':
        for alphabet in string:
            upper = alphabet.upper()
            index = letters.find(upper)
            
            if index == -1:
                final +=alphabet
                
            elif index != -1:
                
                index +=SET[count]
                
                while index >=len(letters):
                    index -=len(letters)   
                    
                if upper in letters and alphabet not in letters:
                    final+= letters[index].lower()
                elif upper in letters and alphabet in letters:
                    final += letters[index]
                count+=1
            if count ==len(SET):
                count=0
    elif mode =='decrypt':
        for alphabet in string:
            upper = alphabet.upper()
            index = letters.find(upper)
            
            if index == -1:
                final +=alphabet
                
            elif index != -1:
                
                index -=SET[count]
                
                while index <0:
                    index +=len(letters)   
                    
                if upper in letters and alphabet not in letters:
                    final+= letters[index].lower()
                elif upper in letters and alphabet in letters:
                    final += letters[index]
                count+=1
            if count ==len(SET):
                count=0        
        
        
    return final