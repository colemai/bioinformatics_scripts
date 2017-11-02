#!/usr/bin/python3

from sys import argv

dna_seq = argv[1]
rna_seq = ''

for i in range(0, len(dna_seq)):
	if dna_seq[i] == 'T':
		rna_seq += 'U'
	else:
		rna_seq += dna_seq[i]

print(rna_seq)

