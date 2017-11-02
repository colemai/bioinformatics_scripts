#!/usr/bin/python3

#Expected input of a single stringed NT sequence

from sys import argv

dna_seq = argv[1]
output_seq = ''

reversed_dna_seq = dna_seq[::-1]

for i in range(0, len(dna_seq)):
	if reversed_dna_seq[i] == 'T': output_seq += 'A'
	elif reversed_dna_seq[i] == 'A': output_seq += 'T'
	elif reversed_dna_seq[i] == 'G': output_seq += 'C'
	elif reversed_dna_seq[i] == 'C': output_seq += 'G'

print(output_seq)

