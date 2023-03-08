"""Generate Markov text from text files."""
import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = open(file_path).read() 

    return contents 


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
   
    words = text_string.split()
    # print(words)

    # fake_words = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    # n = 3 

    for i in range(len(words) - n):
        ngram_list = []
        for j in range(i, i+n):
            ngram_list.append(words[j]) 
        ngram_str = ' '.join(ngram_list) 
        # print(ngram_str)
        
        # bigram_tuple = (words[i], words[i+1])

        if ngram_str in chains:
            chains[ngram_str].append(words[i+n]) 
        else:
            chains[ngram_str] = [words[i+n]] 


    return chains


def make_text(chains):
    """Return text from chains."""

    words = [] 

    chains_keys = list(chains.keys()) 
    initial_key = choice(chains_keys) 
    initial_key_list = initial_key.split(' ')
    new_key = ' '.join(initial_key_list[1:]) + ' ' + choice(chains[initial_key])
    # new_key = (random_key[1], choice(chains[random_key]))  

    while new_key in chains: 
        words.append(choice(chains[new_key])) 
        new_key_list = new_key.split(' ')
        new_key = ' '.join(new_key_list[1:]) + ' ' + choice(chains[new_key])
        # new_key = (new_key[1], choice(chains[new_key])) 
    
    return ' '.join(words)

user_input = input("What value do you want to use for n? ") 

# input_path = 'gettysburg.txt'
input_path = sys.argv[1]
# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, int(user_input))

# Produce random text
random_text = make_text(chains)

print(random_text)
