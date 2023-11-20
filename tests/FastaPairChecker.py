# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 14:57:10 2023

@author: Alexander G Lucaci
"""

import pandas as pd
import numpy as np
import os
import json
import argparse
from Bio import SeqIO

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#end class

ORIGINAL_FILE = "REM2_AA.fasta"
SECOND_FILE   = "TestFO_AA.fasta"

original_sequences = SeqIO.parse(open(ORIGINAL_FILE),'fasta')

def GetComparatorSequence(fasta, _id):
    compare_sequences  = SeqIO.parse(open(SECOND_FILE),'fasta')
    for record in compare_sequences:
        if record.id == _id:
            return record.seq
        #end if
    #end for
    return "N/A"
#end method
    
_errors = []
count   = 0
for record in original_sequences:
    #print(record.id)
    #print(record.seq)
    comp_seq = GetComparatorSequence(SECOND_FILE, record.id)
    
    if record.seq == comp_seq:
        print(bcolors.OKBLUE + "Match!" + bcolors.ENDC, record.id)
    else:
        print(bcolors.WARNING + "No Match!" + bcolors.ENDC, record.id)
        _errors.append(record.id)
    #end if
    count += 1
#end for

if _errors:
    print("Errors found in:", len(_errors))
    print(_errors)
else:
    print("Complete match in", count, "sequences!")
#end if

#print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
#print(bcolors.OKBLUE + "Match!")
#print(bcolors.WARNING + "No Match!")

#with open(output_file) as out_file:
#    for fasta in fasta_sequences:
#        name, sequence = fasta.id, str(fasta.seq)
#        new_sequence = some_function(sequence)
#        write_fasta(out_file)