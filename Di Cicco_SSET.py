'''
Rosalind SSET exercise by Di Cicco Cecilia
'''
# Counting Subsets

# Defining the count_subsets_modulo function that takes an integer n as input and returns the number of subsets of a set with n elements modulo 1,000,000

def count_subsets_modulo(num): 
    result = 1
    for i in range(num):
        result = (result * 2) % 1_000_000
    return result

if __name__ == "__main__":
    num = 938
    output = count_subsets_modulo(num)
    print(output)
