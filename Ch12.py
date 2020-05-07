UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n' 

def load_dict(filename):
    dick = open(filename+'.txt' ,'r')
    words = dick.read().split('\n')
    english={}
    for word in words:
        english[word]=None
    dick.close()
    return english
        
    
ENGLISH_WORDS = load_dict('dictionary')

def remove_non_letters(string):
    L=[]
    for character in string:
        if character in LETTERS_AND_SPACE:
            L.append(character)
    return ''.join(L)

def get_english_count(string):
    string = string.upper()
    string = remove_non_letters(string)
    words = string.split()
    if len(words) ==0:
        return 0
    
    elif len(words)>0:
        count=0
        for word in words:
            if word in ENGLISH_WORDS:
                count+=1
        return round(float(count/len(words)),3)
    
def is_english(string, wordPercentage=20, letterPercentage=85):
    eng_words = get_english_count(string)*100
    if eng_words< wordPercentage:
        return 0
    num_letters = len(remove_non_letters(string))
    messageLettersPercentage = round(float((num_letters) / len(string)),3) * 100
    if messageLettersPercentage < letterPercentage:
        return 0
    else:
        lettersMatch = messageLettersPercentage >= letterPercentage
    return 1
        
    