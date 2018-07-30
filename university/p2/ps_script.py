#!/usr/bin/python3
"""
author: Ian Coleman
student_number: 910616160090
purpose: Parse GenBank file and output two summary files
"""

import re
from sys import argv

def genbank_to_summary (genbank_file):
    #Turns a genbank file into a list of dictionaries, each dict is summary info for a record
    #Output = [{'Accession':'', "ORGANISM": '', SEQUENCE: 'agct'}]
    with open(genbank_file, 'r') as file_object:
        file_list = file_object.readlines()
        records_list = []
        record_number = 0
        sequence_trigger = 0
        for i in range(0, len(file_list)):
            #iterate through gb file and make dict of pertinient info on each record
            if file_list[i].startswith('ACCESSION'):
                accessions = ' '.join(file_list[i].strip().split(' ')[3:])
                records_list.insert(record_number, {'ACCESSION' : accessions})
            elif file_list[i].startswith('  ORGANISM'):
                records_list[record_number]['ORGANISM'] = file_list[i].strip()[10:]
            elif file_list[i].startswith('ORIGIN'):
                sequence_trigger = 1
            #iterate through each of the next lines until line with // and strip numbers and join seqs
            elif file_list[i].startswith('//'):
                sequence_trigger = 0
                record_number += 1
            elif sequence_trigger == 1:
                records_list[record_number].setdefault('SEQUENCE', '')
                records_list[record_number]['SEQUENCE'] += re.sub('[^A-Za-z]+', '', file_list[i].strip())
        return records_list
        
def gc_content_genbank_summary (genbank_list):
    #Takes a genbank summary list and adds gc content entries
    #Output = [{'Accession':'', "ORGANISM": '', 'SEQUENCE': 'agct', 'GC_CONTENT': 67.12 }]
    for i in range(0, len(genbank_list)):
        gc_count = genbank_list[i]['SEQUENCE'].count('c') + genbank_list[i]['SEQUENCE'].count('g')
        gc_percentage = round(gc_count/len(genbank_list[i]['SEQUENCE']) * 100, 2)
        genbank_list[i]['GC_CONTENT'] = gc_percentage
    return genbank_list
        
def seq_length_genbank_summary (genbank_list):
    #Takes a genbank summary list and adds seq length entries. 
    for i in range(0, len(genbank_list)):
        genbank_list[i]['SEQ_LENGTH'] = len(genbank_list[i]['SEQUENCE'])
    return (genbank_list)

def gc_order_genbank_summary (genbank_list):
    #Take a genbank summary list and order it by the gc content of its records
    changes = 1
    while changes > 0:
        changes = 0
        for i in range(0, len(genbank_list) - 1):
            if genbank_list[i]['GC_CONTENT'] < genbank_list[i + 1]['GC_CONTENT']:
                genbank_list[i], genbank_list[i+1] = genbank_list[i+1], genbank_list[i]
                changes += 1
            else:
                continue
    return genbank_list 

def genbank_parse_master (gb_file):
    #Run the set of methods to take a genbank file and output it as a list of dicts, ordered by gc content
    #Output = [{'Accession':'', "ORGANISM": '', 'SEQUENCE': 'agct', 'GC_CONTENT': 67.12, 'SEQ_LENGTH': 2}]
    genbank_list = genbank_to_summary(gb_file)
    genbank_list_2 = gc_content_genbank_summary (genbank_list)
    genbank_list_3 = seq_length_genbank_summary (genbank_list_2)
    genbank_list_4 = gc_order_genbank_summary(genbank_list_3)
    return genbank_list_4   


def output_fasta_from_genbank (genbank_list):
    #Take a list of dicts summarising genbank records, output fasta file 'genbank.fasta'
    with open('genbank.fasta', 'w') as file_object:
        for i in range(0, len(genbank_list)):
            label = '>' + (genbank_list[i]['ACCESSION'] + ' ' + genbank_list[i]['ORGANISM']) + '\n'
            seq = genbank_list[i]['SEQUENCE'].upper() + '\n'
            file_object.write(label)
            file_object.write(seq)

def output_tabbed_file_from_gebank (genbank_list):
    #Take a list of dicts summarising genbank records, output tab delimited file 'genbank_summary.txt'
    with open('genbank_summary.txt', 'w') as file_object:
        for i in range(0, len(genbank_list)):
            accession = genbank_list[i]['ACCESSION'] + '\t'
            organism = genbank_list[i]['ORGANISM'] + '\t'
            gc_content = str(genbank_list[i]['GC_CONTENT']) + '\t'
            seq_length = str(genbank_list[i]['SEQ_LENGTH'])
            file_object.write(accession)
            file_object.write(organism)
            file_object.write(gc_content)
            file_object.write(seq_length)
            file_object.write('\n')

if __name__ == "__main__":
    genbank_list = genbank_parse_master(argv[1])
    output_fasta_from_genbank(genbank_list)
    output_tabbed_file_from_gebank(genbank_list)