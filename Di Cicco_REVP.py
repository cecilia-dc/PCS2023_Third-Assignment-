'''
Rosalind REVP exercise by Di Cicco Cecilia
'''
# Locating Restriction Sites

def rev_complement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join(complement[base] for base in reversed(s))

def find_rev_palindromes(DNA):
    results = []
    for i in range(len(DNA)):
        for j in range(4, 13):  # the reverse palindrome has a length between 4 and 12, inclusive
            if i + j <= len(DNA):
                sequence = DNA[i:i+j]
                reverse_sequence = rev_complement(sequence)
                if sequence == reverse_sequence:
                    results.append((i + 1, j))
    return results

# input string of DNA
dna_string = 'CGCGTGAGTCAATTGGCTACTTTTCCGCGATTCCTGGTGGGATCTGTCAAATTCACGTTTTTGGGAGGACAGAACTGCCGGTCCTCATGGACGGACAGCACCTGTGCCTTGGTAGGTACGCAGGGCCAGTGGTCTTAATCCGCTAAAGATATGCACGCTTAGTGTTAGAATAATTTATCGCGCGTGCGATACTGAATCCTAAGGCTAATTCCTGTCGTTTCACGTCTTAGCCGAGTCCGTGTCCATTGTTGTATTTTGCCTTCGACGAGCAAGCTGCAGGGGGGTAATCGACGGGTCGATGTTGCGCACTTACGGTGACATGCGTTCCGCGTAAACGTAAGCAAGTTACTGCACTATGTACACTGCTAAACTAAATCCTCGGACTGTCCAATTACCATGGTACAGTGCAGCCTTTATGATTGGTTAATATATTCTCGCTGAGCAATTATCCCGCGGGGGAGATACGGTTAGTACTAACTCAGCGTAAAGGTGGTAATAGGTGAATACCAATCTCCCCGCTTCGTCTATTGTGGCCGAGTCAGCGGGAACTTTGCGAAAAAGTTGAATCACCCGGACATCACCTCCAAGGGTAATACTTACGCAAAGGCCGATCATATACATTTGCCTCCTCGAGCATACTACTGTGAGAAATCGGAACTTATTCGTCTGAGTGCCGAACAGTGAGTTTCGTCCTCAGATTCCGGACGCGACTTTTCTGAATTCCTAAAACGAACACCCCAATGGGTGCTTAGCACCTGCACACGTCTTGTTGGGTCTGGAATGACCCAACTATATGTGGGTGGCGTATAGTATTATCCAGGCCGACATTTGGTGTATGGAAAGGATCCAAGGTAACCACGCATCACCACTCGGGCTCCGGAGAGGCCAGTTGCGCCCACCCTGGATACACCCCTGAAACGCAGCACTTGGACTTTCTCGTGCGC'
result = find_rev_palindromes(dna_string)

for position, length in result:
    print(position, length)
