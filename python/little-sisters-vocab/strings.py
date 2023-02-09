#SOLVED
'''Module docstring makes exercism happy'''
def add_prefix_un(word):
    '''easy, just add un '''
    return "un" + word

def make_word_groups(vocab_words):
    '''obligatory docstring,renamed x to counter'''
    puffer = []
    newlist = []
    i = 1
    counter = len(vocab_words)
    while i < counter :
        puffer = vocab_words[0] + vocab_words[i]
        i += 1
        newlist.append(puffer)
    return str(vocab_words[0] + " :: " + " :: ".join(newlist))

def remove_suffix_ness(word):
    '''yeeehah,another docstring is important'''
    if word[-5] == "i" :
        return word[0:-5] + "y"
    return word[0:-4]

def noun_to_verb(sentence, index):
    '''This was really easy.'''
    liste = sentence.split()
    wrd = liste[index]
    if wrd[-1] == "." :
        wrd = wrd[0:-1]
    word = wrd + "en"
    return word
