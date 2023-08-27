import os
import sys


BASEDIR = os.getcwd()

print(BASEDIR)

input_data = os.path.join(BASEDIR, "data", "REM2_DNA.fasta")

print(input_data)

filename = "REM2_DNA.fasta"

os.makedirs(os.path.join(BASEDIR, "results"), exist_ok = True)
os.makedirs(os.path.join(BASEDIR, "results", "TN93"), exist_ok = True)

rule all:
    os.path.join(BASEDIR, "results", "TN93", filename + ".dst")


rule tn93:
    input:
       input = input_data
    output:
       output = os.path.join(BASEDIR, "results", "TN93", filename + ".dst")
    shell:
       "tn93 -t 1 -o {output.output} {input.input}"
    #end shell
#end rule

