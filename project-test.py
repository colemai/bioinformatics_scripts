from sys import argv
import pdb
import os
import subprocess

fastq_pairs_path = argv[1]
stringer = ''

for item in os.listdir(fastq_pairs_path):
	print(item)
	stringer += (' ../il_reads' + item)

print(stringer)