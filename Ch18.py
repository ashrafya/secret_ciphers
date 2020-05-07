import pprint, time, copy, re, wordPatterns

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
non_letter_space = re.compile('[^A-Z\s]')

probs={'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': ['U', 'O', 'A', 'I'], 'H': ['P', 'B', 'L', 'N'], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': ['Y', 'S'], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []} 

def word_pattern(string):
    '''
    takes in a word and return the pattern it has, in terms of what letters are used
    '''
    string = string.upper()
    final = []
    DICT = {}
    count=0
    for letter in string:
        if letter not in DICT:
            DICT[letter]= str(count)
            count+=1
        final.append(DICT[letter])
    return ','.join(final)

def all_patterns():
    f = open('dictionary.txt','r')
    contents = f.read().split('\n')
    f.close()
    L = []
    for word in contents:
        pattern = word_pattern(word)
        if pattern not in L:
            L.append(pattern)
        elif pattern in L:
            continue

def get_similar_words(string):
    tic = float(time.time())
    
    similar = {}
    f = open('dictionary.txt', 'r')
    contents = f.read().split('\n')
    f.close()
    OG = word_pattern(string)
    for word in contents:
        pattern = word_pattern(word)
        if OG == pattern:
            if OG not in similar:
                similar[OG] = [word]
            elif OG in similar:
                similar[OG].append(word)
    toc =float(time.time())
    print('it took %s seconds\n' %round(toc-tic, 3))
    return similar,len(similar[OG])
            
def blank_cipher():
    return probs

def add_to_mapping(letter_mapping, word, possible):
    #letter_mapping is a letter mapping dictionary value that is the return value
    #of this function. 
    #word is the encrypted word
    #candidate is a possible english word with the same base structure
    letter_mapping= copy.deepcopy(letter_mapping)
    for j in range(len(word)):
        if possible[j] not in letter_mapping[word[j]]:
            letter_mapping[word[j]].append(possible[j])
    return letter_mapping
        
        
def intersect_mapping(map1, map2):
    '''
    returns only the possible maps of each letter that are present in both
    mappings
    '''
    intersection = blank_cipher()
    for letter in LETTERS:
        if map1[letter] == []: # if empty, means letter can be mapped to anything
            intersection[letter] = copy.deepcopy(map2[letter])
        elif map2[letter] == []:
            intersection[letter] = copy.deepcopy(map1[letter])
        else:
            for mapped in map1[letter]:
                if mapped in map2[letter]: # only add to intersection if present
                    #in both map1 and map2
                    intersection[letter].append[mapped]
    return intersection


def remove_solved(mapping):
    # Cipher letters in the mapping that map to only one letter are
    # "solved" and can be removed from the other letters.
    # For example, if 'A' maps to potential letters ['M', 'N'], and 'B'
    # maps to ['N'], then we know that 'B' must map to 'N', so we can
    # remove 'N' from the list of what 'A' could map to. So 'A' then maps
    # to ['M']. Note that now that 'A' maps to only one letter, we can
    # remove 'M' from the list of letters for every other
    # letter. (This is why there is a loop that keeps reducing the map.)    
    mapping = copy.deepcopy(mapping)
    going = True
    while going:
        going = False #will determine if need to loop again
        solved = [] #only letter with one mapping will enter here
        for letter in LETTERS:
            if len(mapping[letter]) == 1:
                solve.append(mapping[letter][0])
        #now remove from all other keys
        
        for letter in LETTERS:
            for s in solved:
                if len(mapping[letter]) !=1 and s in mapping[letter]:
                    mapping[letter].remove(s)
                    if len(mapping[letter]) == 1:
                        #found another solved letter so go again
                        going = True
    return mapping
                
def hack_sub(string):
    
    intersection = blank_cipher()
    encrypted_list = non_letter_space.sub('', string.upper()).split()
    for word in encrypted_list:
        new = blank_cipher()
        
        pattern = word_pattern(word)
        if pattern not in wordPatterns.allPatterns:
            continue
        for possible in wordPatterns.allPatterns[pattern]:
            new = add_to_mapping(new, word, possible)
        intersection = intersect_mapping(intersection, new)
    return remove_solved(intersection)

