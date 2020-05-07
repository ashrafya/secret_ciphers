englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'



def letter_count(message):
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter] += 1

    return letterCount


def item_at_zero(x):
    return x[0]

def freq_order(string):
    letter_freq = letter_count(string)
    
    freq_to_letter={}
    for letter in LETTERS:
        if letter_freq[letter] not in freq_to_letter:
            freq_to_letter[letter_freq[letter]] = [letter]
        else:
            freq_to_letter[letter_freq[letter]].append(letter)
    
    for number in freq_to_letter:
        freq_to_letter[number].sort(key=ETAOIN.find, reverse=True)
        freq_to_letter[number] = ''.join(freq_to_letter[number])
    
    pairs = list(freq_to_letter.items())
    pairs.sort(key = item_at_zero, reverse=True)
    
    freq_order=[]
    for pair in pairs:
        freq_order.append(pair[1])
    
    return ''.join(freq_order)

def english_freq_match(string):
    freqOrder = freq_order(string)
    
    match=0
    
    for common in ETAOIN[:6]:
        if common in freqOrder[:6]:
            match+=1
    for common in ETAOIN[-6:]:
        if common in freqOrder[-6:]:
            match+=1 
            
    return match