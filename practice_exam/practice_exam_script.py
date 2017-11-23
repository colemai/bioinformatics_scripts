#!/usr/bin/python3
"""
Author: Ian Coleman
Student Number: 910616160090

Inputs: Two fasta files, first is a reference, second is assembled contigs
"""

from sys import argv
import subprocess
import re


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
#Step4 Calculate N50 index
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

#Step5 Calcualte compare the two assemblies using lastz
#create and call the lastz command on the terminal TODO checks this work
# cmd = 'lastz --format=general --output={}  {} {}'.format('outlastz.txt', argv[1], argv[2])
# subprocess.check_call(cmd, shell=True)
#TODO CHECK WHETHER OUTPUT FILE EXISTS and if so don't run code to create it

def intake_alignment_coordinates (input_filename):
    """
    Input: Lastz output file (general format)
    Output: Alignment coordinates in list of tuples [(start_of_alignment, end_of_alignment)]
    """
    list_coordinates = []
    with open(input_filename, 'r') as file_object:
        file_list = file_object.readlines()
        for line in file_list[1:]:
            list_coordinates.append((int(line.split()[4]), int(line.split()[5])))
    return (list_coordinates)
        #Get a list of tuples of the sections of the alignments DONE
        #ensure that they align as expected i.e 0 index
        #replace each alignment char with '-'

def replace_aligned_sections (reference_sequence, coordinates):
    """
    Input: Sequence of reference as str, Coordinates in list of tuples
    Output: String with - replacing each char in an alignment
    """
    alignments_length_tuples = []
    # for key, value in coordinates.items():
    #     alignments_length_tuples.append((key, len(value)))
    alignments_by_size = sorted(coordinates, key=lambda k: k[0])
    # print(alignments_by_size[1][0])
    # print(alignments_by_size[1][0], alignments_by_size[1][1])
    # print(reference_sequence[alignments_by_size[1][0]:alignments_by_size[1][1]])
    for coord in alignments_by_size:
        align_begin = coord[0]
        align_end = coord[1]
        align_length = align_end - align_begin
        reference_sequence = reference_sequence[:align_begin] + (align_length * '!') + reference_sequence[align_end:]
    unaligned_segments = re.finditer('[CATG]+', reference_sequence)
    uncovered_bases = 0
    for segment in unaligned_segments:
        print (segment.start(), ':', segment.end(), segment.group(0))

#Step6 Find the regions from the reference genome that are not covered by the Velvet assembly

#Step7 if time do some testing, asserts
#Assert that two argv's given

if __name__ == "__main__":
    reference = parse_fasta(argv[1])
    assembled_contigs = parse_fasta(argv[2])
    size_of_assembly = assembly_size(assembled_contigs)
    n50_score = n50_and_n50_index(assembled_contigs, size_of_assembly)[0]
    n50_index = n50_and_n50_index(assembled_contigs, size_of_assembly)[1]
    alignment_coordinates = intake_alignment_coordinates('outlastz.txt')
    for key,val in reference.items():
        unaligned_segments = replace_aligned_sections(val, alignment_coordinates)

    # print(n50_score)


#TODO get the n50 scores for the refernce genome as well for some reason