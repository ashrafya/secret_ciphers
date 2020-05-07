import time, re, Ch12, Ch21, Ch20

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
SILENT_MODE = False # if set to True, program doesn't print attempts
NUM_MOST_FREQ_LETTERS = 4 # attempts this many letters per subkey
MAX_KEY_LENGTH = 16 # will not attempt keys longer than this
NONLETTERS_PATTERN = re.compile('[^A-Z^a-z]')

def repeat_sequence(string):
    string = NONLETTERS_PATTERN.sub('', string.upper())
    
    seq_and_spacings = {}
    tic= time.time()
    
    for length in range(3,6):
        for seqStart in range(len(string) - length):
            
            seq = string[seqStart:seqStart + length]
            #goes from the start till the length of the sequence and goes through
            #the whole string like this, incrementing by one
            
            for i in range(seqStart +length, len(string)-length):
                # minus length because want to have enough at the end to read 
                
                if string[i:i+length] == seq:
                    if seq not in seq_and_spacings:
                        seq_and_spacings[seq] = []
                    seq_and_spacings[seq].append(i-seqStart)
    toc = time.time()
    #print('it took %s second' %round(toc-tic,3))
    #print()
    return seq_and_spacings


def useful_factors(number, key_length):
    tic = time.time()
    
    if number<2:
        return []
    factors=[]
    
    for i in range(2, key_length+1):
        if number%i ==0:
            factors.append(i)
            factors.append(int(number/i))
    if 1 in factors:
        factors.remove(1)
    toc = time.time()
    print('it took %s second' %round(toc-tic,3))
    print()
    #for i in range(len(factors)):
        #for j in range(i+1, len(factors)):
            #if factors[i] == factors[j]:
                #factors[j] = None
                
    #while None in factors:
        #factors.remove(None)
            
    return factors           
                
def index_at_one(x):
    return x[1]

def most_common_factors(seqFactors, max_key_length):
    factor_counts={}
    
    for seq in seqFactors:
        factor_list= list(seqFactors[seq])
        
        for factpr in factor_list:
            if factor not in factor_counts:
                factor_count[factor]=0
            else:
                facto_count[factor]+=1
                
    factor_by_count=[]
    
    for factor in factor_counts:
        if factor <= max_key_length:
            factor_by_count.append((factor, factor_counts[factor]))
    factor_by_count.sort(key=index_at_one, reverse=True)
    return factor_by_count
        


def kasiskiExamination(string, key_length):
    repeated_seq_spacing = repeat_sequence(string)
    
    seq_factors ={}
    
    for seq in repeated_seq_spacings:
        seq_factors[seq] = []
        for spacing in repeated_seq_spacing[seq]:
            seq_factors[seq].extend(useful_factors(spacing, key_length))
    
    factors_by_count = most_common_factors(seq_factors, key_length)
    
    likey=[]
    
    for element in factors_by_count:
        likely.append(element[0])
    return likely

def sub_key_letters(n, length, string):
    
    string = NONLETTERS_PATTERN.sub('', string)
    print(string)
    index = n-1
    
    letter=[]
    while index<len(string):
        letter.append(string[index])
        index+=length
    return ''.join(letter)