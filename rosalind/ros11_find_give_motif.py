#!/usr/bin/env python3
"""
Author: Ian Coleman
Purpose: Take a file of uniprot_ids, find the occurences of the n-glycosylation motif
"""

from sys import argv
import urllib.request
import re 


#Step1 Turn the input into a list of uniprot IDs
def input_into_list (input_file):
    """
    Input: A file of uniprot IDs (one per line)
    Output: A list of uniprot IDs
    """
    uniprot_ids = []
    with open(input_file) as file_object:
        lines = file_object.readlines()
        for line in lines:
            uniprot_ids.append(line.strip())
    return uniprot_ids

#Step2 Take the list of uniprot IDs and get their sequences
def uniprot_id_to_fasta_list (uniprot_id):
    """
    Input: A uniprot id
    Output: A dictionary {'Label': fasta_label, 'Sequence': sequence] for that protein
    """
    #Assert that the url exists
    fasta_list = {}
    #fetch the fasta for this id from the uniprot site, make the required list
    with urllib.request.urlopen('http://www.uniprot.org/uniprot/%s.fasta' % uniprot_id) as response:
        html = response.readlines()
        sequence = ''
        for line in html[1:]:   
            sequence += (line.decode('UTF-8').strip())
        label = html[0].decode('UTF-8').strip()
        fasta_list = {'Label': label, 'Sequence': sequence}
    return (fasta_list)

def uniprot_ids_to_dict (uniprot_ids):
    """
    Input: Uniprot id list
    Output: Dictionary {}
    """
    protein_dict = {}
    for uniprot_id in uniprot_ids:
        protein_dict[uniprot_id] = uniprot_id_to_fasta_list(uniprot_id)
    return(protein_dict)

#Step3 Find the occurences of the n-glycosylation motif  in each sequence
def find_motif_occurences (sequence, motif_regex):
    """
    Input: A protein sequence, a motif
    Output: List of occurences of given motif in given sequence
    """
    locations = []
    pattern = re.compile(motif_regex)
    for match in pattern.finditer(sequence):
        locations.append(str(match.start() + 1))
    return(' '.join(locations))

#Step5 call methods
uniprot_ids = input_into_list(argv[1])
protein_dict = uniprot_ids_to_dict(uniprot_ids)
motif = '(?=(N[^P][TS][^P]))'

for uniprot_id in uniprot_ids:
    if find_motif_occurences(protein_dict[uniprot_id]['Sequence'], motif) != '':
        print (uniprot_id)
        print (find_motif_occurences(protein_dict[uniprot_id]['Sequence'], motif))
