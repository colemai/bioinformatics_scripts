#!usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Transcribe DNA into any ORF in the 6 RFs
Input: Single DNA NT sequence in Fasta format
Output:
"""

from sys import argv

#Step1: Take in Fasta and get NT seq of forward DNA Strand
def single_fasta_to_string (input_file):
	with open(input_file) as fasta_file:
		lines = fasta_file.readlines()
		forward_sequence = lines[1]
	return(forward_sequence)


#Step2: Use forward DNA strand to calculate reverse complement strand
def generate_reverse_complement_dna (forward_sequence):
	"""
	Input: Dna sequence as string
	Output: The reverse complement of that sequence as a string
	"""
	reverse_complement = ''
	reverse_forward_sequence = forward_sequence[::-1]
	dna_dict = {
		'A':'T',
		'T':'A',
		'G':'C',
		'C':'G'
	}
	for nt in reverse_forward_sequence:
		 reverse_complement += dna_dict.get(nt)
	return reverse_complement


#Step3: Convert to RNA
def dna_to_rna(dna_seq):
	return dna_seq.replace('T', 'U')

#Step4: Calculate reading frames 
def seq_to_reading_frames (dna_seq):
	"""
	Input: a single dna seq as string
	Output: a list of three reading frames
	"""
	rf_1 = dna_seq
	rf_2 = dna_seq[1:]
	rf_3 = dna_seq[2:]
	rf_list = [rf_1, rf_2, rf_3]
	return rf_list


#Step5: Turn list of RNA reading frames into list of proteins (one for each ORF)
def rna_to_aa_case (rna_codon):
	"""
	Input: An RNA codon
	Output: the corresponding AA (represented by a single letter)
	Note: 'Stop' will be returned by a stop codon
	"""

	return {
		'AUG': 'R',
		'UUU': 'F',      
		'CUU': 'L',
		'AUU': 'I',      
		'GUU': 'V',
		'UUC': 'F',
		'CUC': 'L',
		'AUC': 'I',      
		'GUC': 'V',
		'UUA': 'L',      
		'CUA': 'L',
		'AUA': 'I',
		'GUA': 'V',
		'UUG': 'L',      
		'CUG': 'L',
		'AUG': 'M',
		'GUG': 'V',
		'UCU': 'S' ,     
		'CCU': 'P',
		'ACU': 'T',
		'GCU': 'A',
		'UCC': 'S' ,     
		'CCC': 'P',
		'ACC': 'T',
		'GCC': 'A',
		'UCA': 'S' ,     
		'CCA': 'P',
		'ACA': 'T',
		'GCA': 'A',
		'UCG': 'S' ,     
		'CCG': 'P',
		'ACG': 'T',
		'GCG': 'A',
		'UAU': 'Y' ,     
		'CAU': 'H',
		'AAU': 'N',
		'GAU': 'D',
		'UAC': 'Y' ,     
		'CAC': 'H',
		'AAC': 'N',
		'GAC': 'D',
		'UAA': 'Stop',   
		'CAA': 'Q',
		'AAA': 'K',
		'GAA': 'E',
		'UAG': 'Stop',  
		'CAG': 'Q',
		'AAG': 'K',
		'GAG': 'E',
		'UGU': 'C',      
		'CGU': 'R',
		'AGU': 'S',
		'GGU': 'G',
		'UGC': 'C',      
		'CGC': 'R',
		'AGC': 'S',
		'GGC': 'G',
		'UGA': 'Stop',   
		'CGA': 'R',
		'AGA': 'R',
		'GGA': 'G',
		'UGG': 'W',      
		'CGG': 'R',
		'AGG': 'R',
		'GGG': 'G'
	}.get(rna_codon, '')

def rna_to_codons(rna_string):
	"""
	Input: RNA string (or any string)
	Output: List of codons (string split into sets of three chars)
	Note: If string is not divisible by three then the last codon will be one or two chars
	"""
	codon_list = []
	for i in range(0, len(rna_string), 3):
		codon_list.append(rna_string[i:i+3])
	return (codon_list)

def translate_all_ORFs (rf_list):
	"""
	Input: List of RNA reading frames
	Output: List of AA seqs resulting from all open reading frames of these RFs
	"""
	aa_seq_list = []
	#iterate through reading frames
	for rf in rf_list:
		transient_list = []
		switch = 0
		codons = rna_to_codons(rf)
		#iterate through codons for this RF, translate each and take any seq between start and stop codon
		for codon in codons:
			if codon == "AUG":
				switch += 1
				transient_list.insert(switch -1, 'M')
			elif rna_to_aa_case(codon) == 'Stop':
				aa_seq_list += transient_list
				switch = 0
			elif switch > 0:
				for i in range(0, len(transient_list)):
					transient_list[i] += (rna_to_aa_case(codon))
			else:
				continue
	return (set(aa_seq_list))

#Step6: Output

if __name__ == "__main__":
	forward_sequence = single_fasta_to_string(argv[1])
	reverse_complement = generate_reverse_complement_dna(forward_sequence)

	rna_forward_strand = dna_to_rna(forward_sequence)
	rna_reverse_strand = dna_to_rna(reverse_complement)

	rf_list = seq_to_reading_frames(rna_forward_strand) + seq_to_reading_frames(rna_reverse_strand)
	proteins = translate_all_ORFs(rf_list)

	for seq in proteins:
		print (seq)
