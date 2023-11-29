'''
Rosalind LEXF exercise by Di Cicco Cecilia
'''
# Enumerating k-mers Lexicographically

from itertools import product # the product function from itertools generates all possible combinations with the given alphabet and length

def generate_strings(alphabet, length):
    return [''.join(p) for p in product(alphabet, repeat=length)]

def main(): # input dataset
    alphabet = ['A', 'B', 'C', 'D']
    length = 4

    # generating and printing all strings in lexicographical order
    strings = generate_strings(alphabet, length) 
    for s in strings:
        print(s)

if __name__ == "__main__":
    main()
