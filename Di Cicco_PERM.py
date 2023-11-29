'''
Rosalind PERM exercise by Di Cicco Cecilia
'''
# Enumerating Gene Orders

from itertools import permutations # using iterators

def permutation(n):
    # Generate all permutations of the numbers from 1 to n
    perms = list(permutations(range(1, n + 1)))

    print(len(perms)) # total number of permutations

    for p in perms:
        print(' '.join(map(str, p)))

permutation(5)

