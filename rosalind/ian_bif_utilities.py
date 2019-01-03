#!/usr/bin/python3

from sys import argv
import numpy as np

def fasta_to_dict (input_filename):
    """
    Input: Fasta File
    Output: Dictionary of {label: sequence} both strings
    """
    with open(input_filename, 'r') as file_object:
        file_list = file_object.readlines()
        fasta_dict = {}
        for i in range(0, len(file_list)):
            if file_list[i].startswith('>'):
                label_index = file_list[i].strip()[1:]
                fasta_dict[label_index] = ''
            else: 
                fasta_dict[label_index] += file_list[i].strip()
        return fasta_dict

def single_fasta_to_string (input_file):
    """
    Input: Fasta file with single fasta entry
    Output: Sequence string
    """
    with open(input_file) as fasta_file:
        lines = fasta_file.readlines()
        #get the stripped version of every line after the first line joined up
        forward_sequence = ''.join(list(map(str.strip, lines[1:])))
    return(forward_sequence)

def fasta_to_list (file_path):
    """
    Input: Path to fasta file with multiple DNA seqs of equal length
    Output: List of seqs
    """
    with open(file_path, 'r') as file_object:
        lines_list = file_object.readlines()
        seq_list = []
        current_seq = ''
        for line in lines_list:
            if line.startswith('>'):
                seq_list.append('')
                current_seq = ''
            else:
                seq_list[-1] += line.strip()
        return seq_list

def import_string(file_path):
    """
    Input: Path to text file with single string
    Output: Single string
    """
    with open(file_path) as file_object:
        lines = file_object.readlines()
        polypeptide = lines[0].strip()
    return polypeptide

def get_input_ints(txt_path):
    """
    REQUIRES: Numpy
    Input: path to txt file with multiple ints
    Output: np array of ints
    """
    with open(txt_path, 'r') as txt:
        line = txt.read()
        line = np.asarray(line.split(' ')) # convert input to numpy array
        line = line.astype(np.int) # convert from str to ints
    return line

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
    return (reverse_complement)


def dna_to_rna(dna_seq):
    return dna_seq.replace('T', 'U')


def seq_to_reading_frames (dna_seq):
    """
    Input: a single dna seq as string
    Output: a list of three reading frames (seqs as strings)
    """
    rf_1 = dna_seq
    rf_2 = dna_seq[1:]
    rf_3 = dna_seq[2:]
    rf_list = [rf_1, rf_2, rf_3]
    return rf_list

def codons_to_protein (codons):
    """
    REQUIRES: rna_to_aa function
    Input: List of strings (codons)
    Output: String (protein seq)
    """
    protein = ''
    for codon in codons:
        protein += rna_to_aa(codon)
    return protein

def rna_to_aa (rna_codon):
    """
    Input: An RNA codon (three char str)
    Output: the corresponding AA (represented by a single letter)
    Note: '*' will be returned by a stop codon
    """
    #make uppercase
    return {
        'UUU': 'F',  'CUU': 'L', 'AUU': 'I',      
        'GUU': 'V', 'UUC': 'F',  'CUC': 'L', 'AUC': 'I',      
        'GUC': 'V', 'UUA': 'L',  'CUA': 'L', 'AUA': 'I',
        'GUA': 'V', 'UUG': 'L',  'CUG': 'L', 'AUG': 'M',
        'GUG': 'V', 'UCU': 'S',  'CCU': 'P', 'ACU': 'T',
        'GCU': 'A', 'UCC': 'S',  'CCC': 'P', 'ACC': 'T',
        'GCC': 'A', 'UCA': 'S',  'CCA': 'P', 'ACA': 'T',
        'GCA': 'A', 'UCG': 'S',  'CCG': 'P', 'ACG': 'T',
        'GCG': 'A', 'UAU': 'Y',  'CAU': 'H', 'AAU': 'N',
        'GAU': 'D', 'UAC': 'Y',  'CAC': 'H', 'AAC': 'N',
        'GAC': 'D', 'UAA': '*',  'CAA': 'Q', 'AAA': 'K',
        'GAA': 'E', 'UAG': '*',  'CAG': 'Q', 'AAG': 'K',
        'GAG': 'E', 'UGU': 'C',  'CGU': 'R', 'AGU': 'S',
        'GGU': 'G', 'UGC': 'C',  'CGC': 'R', 'AGC': 'S',
        'GGC': 'G', 'UGA': '*',  'CGA': 'R', 'AGA': 'R',
        'GGA': 'G', 'UGG': 'W',  'CGG': 'R', 'AGG': 'R',
        'GGG': 'G'
    }.get(rna_codon, '')

def aa_to_codons (aa):
    """
    Input: an amino acid single-char symble
    Output: a list of RNA codons that may have coded that AA
    NOTE: Stop codon represented by *
    """
    #TODO make input uppercase
    return {
        'E': ['GAG', 'GAA'], 
        'V': ['GUG', 'GUC', 'GUA', 'GUU'], 
        'H': ['CAC', 'CAU'], 
        'D': ['GAU', 'GAC'], 
        'G': ['GGU', 'GGC', 'GGG', 'GGA'], 
        'S': ['UCU', 'UCA', 'UCG', 'AGU', 'UCC', 'AGC'], 
        'I': ['AUA', 'AUU', 'AUC'], 
        'L': ['CUA', 'UUG', 'CUC', 'CUU', 'CUG', 'UUA'], 
        'C': ['UGC', 'UGU'], 
        'M': ['AUG'], 
        'N': ['AAC', 'AAU'], 
        'A': ['GCC', 'GCG', 'GCA', 'GCU'], 
        'Q': ['CAA', 'CAG'], 
        'Y': ['UAU', 'UAC'], 
        'P': ['CCG', 'CCC', 'CCA', 'CCU'], 
        '*': ['UAA', 'UGA', 'UAG'], 
        'T': ['ACC', 'ACG', 'ACA', 'ACU'], 
        'W': ['UGG'], 
        'K': ['AAA', 'AAG'], 
        'R': ['CGU', 'CGA', 'CGC', 'CGG', 'AGG', 'AGA'], 
        'F': ['UUC', 'UUU']
    }.get(aa, '')

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
                transient_list.insert(switch -1, '')
            if rna_to_aa_case(codon) == 'Stop':
                aa_seq_list += transient_list
                switch = 0
                transient_list = []
            elif switch > 0:
                for i in range(0, len(transient_list)):
                    transient_list[i] += (rna_to_aa_case(codon))
            else:
                continue
    return (set(aa_seq_list))

def print_list_as_elements(lister):
    """
    Input: List
    Output: Prints each element with a space between, one line per list in the list
    """
    for item in lister:
        seq = ''
        for number in item:
            seq += str(number)
            seq += ' '
        print(seq)

def get_kmers (k, seq):
    """
    Get all kmers of length k from a string
    Input: INT k, STRING seq
    Output: LIST of kmers
    """
    kmers = []
    for i in range(0, len(seq) - (k-1)):
        kmers.append(seq[i:i+4])
    return kmers


def peptide_weight (peptide_letter):
    """
    Input: String --> Letter representing a peptide
    Output: Float --> Peptide's monoisotopic mass ignoring water molecule
    """
    peptide_weights = {
        'A':   71.03711,
        'C':   103.00919,
        'D':   115.02694,
        'E':   129.04259,
        'F':   147.06841,
        'G':   57.02146,
        'H':   137.05891,
        'I':   113.08406,
        'K':   128.09496,
        'L':   113.08406,
        'M':   131.04049,
        'N':   114.04293,
        'P':   97.05276,
        'Q':   128.05858,
        'R':   156.10111,
        'S':   87.03203,
        'T':   101.04768,
        'V':   99.06841,
        'W':   186.07931,
        'Y':   163.06333
    }
    return peptide_weights[peptide_letter]


def total_weight (polypeptide):
    """
    NOTE: REQUIRES peptide_weight def ^^
    Input: A string --> polypeptide
    Output: A float --> its total weight (monoisotopic mass, ignoring water molecule)
    """
    weight = 0
    for aa in polypeptide:
        weight += peptide_weight(aa)
    return weight