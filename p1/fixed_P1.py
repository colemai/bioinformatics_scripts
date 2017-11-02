#!/usr/bin/env python3

"""
Author: D.E. Bug
Script to count the number of k-mers in a FASTA file
Output is compared to jellyfish output

Name: Ian Coleman
Student Number: 910616160090

Differences: 

25c20
<         if not line.strip():
---
>         if not line.stripit():
28c23
<             label = line.strip()
---
>             label = line.strip()[1:]
31c26
<             seqs[label] += line.strip()
---
>             seqs[label] += line.strip()[1:]
45c40
<     for label, seq in seqs.items():
---
>     for label, seq in seqs.items()
50c45
<         for i in range(len(seq)-kmer_size + 1):
---
>         for i in range(len(seq)-kmer_size):
79c74
<             print(k, v)
---
>         print(k, v)
90c85
<     cmd = 'jellyfish count -m {} -s 1000000 -o {} {}'\
---
>     cmd = 'jellyphish count -m {} -s 1000000 -o {} {}'\
107c102
<     kmers = extract_kmers(dna_seqs, skip_unknown=True, k=15)
---
>     kmers = extract_kmers(dna_seqs, skip_unknown=True, k=14)
112c107
<     print(str(jelly_out))
---
>     print(str(jelly_out,'utf-8'))
"""

from sys import argv
import subprocess
import os.path

# import code; code.interact(local=dict(globals(), **locals()))

def parse_fasta(lines):
    """Return dictionary of {label:dna_seq}
    
    lines: list of lines in FASTA format
    """
    seqs = {}
    for line in lines:
        if not line.strip():
            continue
        if line.startswith('>'):
            label = line.strip()
            seqs[label] = ""
        else:
            seqs[label] += line.strip()
    return seqs

def extract_kmers(seqs, k=15, skip_unknown=True):
    """Return dict of {kmer_seq: kmer_count}

    seqs: dict of {label:dna_seq}
    k: int, specifying k-mer size
    skip_unknown: bool, specifying wheter k-mers containing 
        non-TGAC characters should be skipped
    """
    kmer_size = k
    ch = {} #dict to store characters
    res = {} #dict to store k-mers and counts
    for label, seq in seqs.items():
        for c in seq:
            if c not in ch:
                ch[c] = 0
            ch[c] += 1
        for i in range(len(seq)-kmer_size + 1):
            kmer = seq[i:i+kmer_size]
            count = True
            for c in kmer:
                if c not in "TGAC":
                    count = False
            if skip_unknown is True and count is False:
                continue
            if kmer not in res:
                res[kmer] = 0
            res[kmer] += 1
    return res

def print_stats(kmer_table):
    """Print the kmer statistics to stdout
    
    kmer_table: dict of {kmer_seq: kmer_count}
    """
    print("MY OUTPUT")
    res = kmer_table
    unique = [i for i, j in res.items() if j==1]
    print("Unique: {}".format(len(unique)))
    print("Distinct: {}".format(len(res)))
    total = sum(res.values())
    print("Total: {}".format(total))
    max_count = max(res.values())
    print("Max count: {}".format(max_count))
    for k, v in res.items():
        if v == max_count:
            print(k, v)
    print('----')
    return None

def run_jellyfish(input_fn, kmer_size=15):
    """Run jellyfish program on fasta file

    input_fn: string, filename of input FASTA file
    kmer_size: int, size of k-mers used by jellyfish
    """
    out_fn = 'tomato{}'.format(kmer_size)
    cmd = 'jellyfish count -m {} -s 1000000 -o {} {}'\
        .format(kmer_size, out_fn, input_fn)
    e = subprocess.check_output(cmd, shell=True)
    if os.path.exists(out_fn):
        cmd = 'jellyfish stats {}'.format(out_fn)
    else:
        cmd = 'jellyfish stats {}'.format(out_fn)
    res = subprocess.check_call(cmd, shell=True)
    return res

if __name__ == "__main__":

    # parse input data
    inp_fn = argv[1]
    dna_seqs = parse_fasta(open(inp_fn))
    # extract k-mers of length 15 and print the results
    kmer_len = 15
    kmers = extract_kmers(dna_seqs, skip_unknown=True, k=15)
    print_stats(kmers)
    # run the tool jellyfish and print the results 
    jelly_out = run_jellyfish(inp_fn, kmer_size=kmer_len)
    print("JELLYFISH OUTPUT")
    print(str(jelly_out))

