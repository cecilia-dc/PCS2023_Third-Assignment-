'''
Rosalind CUNR exercise by Di Cicco Cecilia
'''
# Counting Unrooted Binary Trees


from functools import reduce

# Here we only have  (2n -5)!!
# We can help the calculation by taking the modulo at each step
def cunr(num, mod=10**6):
    return reduce(lambda a, b: a * b % mod, range(2 * num - 5, 1, -2))

num = 928

print(cunr(int(num)))