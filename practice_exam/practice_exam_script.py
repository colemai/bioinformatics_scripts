#!/usr/bin/python3
"""
Author: Ian Coleman
Student Number: 910616160090

Inputs: Two fasta files, first is a reference, second is assembled contigs
"""

from sys import argv


#Step1 Read in both reference and assembly files
def parse_fasta (input_filename):
    """
    Input: Fasta File
    Output: Dictionary of {label: sequence} both strings
    """
    with open(input_filename, 'r') as file_object:
        file_list = file_object.readlines()
        fasta_dict = {}
        for i in range(0, len(file_list)):
            if file_list[i].startswith('>'):
                label_index = file_list[i].strip()
                fasta_dict[file_list[i].strip()] = ''
            else: 
                fasta_dict[label_index] += file_list[i].strip()
        return fasta_dict

#Step2 Calculate  assembly size
def assembly_size (assembly_dict):
    """
    Input: Dict of assembly {Label: Sequence} each as str
    Output: Assembly size as int
    """ 
    size = 0
    for key, value in assembly_dict.items():
        size += len(value)
    return int(size/2)

#Step3 Calculate N50 size
def n50_and_n50_index (assembly_dict, assembly_size):
    """
    Input: Dict of assembly {Label: Sequence} each as str, Assembly size as int
    Output: tuple (n50 size, n50 index) 
    """
    #make list of tuples [(contig_label, length_contig)]
    contigs_length_tuples = []
    for key, value in assembly_dict.items():
        contigs_length_tuples.append((key, len(value)))
    #arrange list by size of value
    contigs_by_size = sorted(contigs_length_tuples, key=lambda k: k[1])

    #Go through list sorted by length, add longest together and add them to contigs_in_50 list
    cumulative_size = 0
    contigs_in_50 = []
    for label,length in contigs_by_size[::-1]:
        if cumulative_size < assembly_size:
            cumulative_size += length
            contigs_in_50.append(length)
        else:
            continue
    #Return the last item added to contigs_in_50 (i.e the smallest length contained) and length 
    return(contigs_in_50[-1], len(contigs_in_50))

#Step4 Calculate N50 index

#Step5 Calcualte compare the two assemblies using lastz

#Step6 Find the regions from the reference genome that are not covered by the Velvet assembly

#Step7 if time do some testing, asserts
#Assert that two argv's given

if __name__ == "__main__":
    reference = parse_fasta(argv[1])
    assembled_contigs = parse_fasta(argv[2])
    size_of_assembly = assembly_size(assembled_contigs)
    n50_score = n50_and_n50_index(assembled_contigs, size_of_assembly)[0]
    n50_index = n50_and_n50_index(assembled_contigs, size_of_assembly)[1]
    print(n50_score)
