'''
Rosalind KMP exercise by Di Cicco Cecilia
'''
# Speeding Up Motif Finding

from Bio import SeqIO

def compute_failure_array(pattern):
    failure = [0] * len(pattern)
    j = 0

    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = failure[j - 1]

        if pattern[i] == pattern[j]:
            j += 1

        failure[i] = j
    failure = str(failure).replace(",", "")
    return failure



# reading the inputfile in FASTA format
input_file = "rosalind_kmp.txt"
with open(input_file, "r") as handle:
    record = SeqIO.read(handle, "fasta")

dna_sequence = str(record.seq)

#print (dna_sequence)
failure_array = compute_failure_array(dna_sequence)

output_file = "output_kmp.txt"
with open(output_file, 'w') as file:
    file.write(failure_array)