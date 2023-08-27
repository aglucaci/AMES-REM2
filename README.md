# Ancestral (Sequence Reconstruction), Molecular Evolution, and Structure


# Input

We use the `data/mammalian_REM2_codons.SA.fasta.SLAC.json` file as input, it is borrowed from the AOC-REM2 analysis.

This file is parsed using the `scripts/ancestralevolution.py` script. Resulting in `data/REM2_AA.fasta`, `data/REM2_DNA.fasta', and `data/REM2_MSA.fasta'

We calculate TN93 genetic distances on the `data/REM2_MSA.fasta' file

A bash command is used to split the multifasta file `data/REM2_DNA.fasta' into single sequence fasta files in `data
/slac_asr`

We then generated PDB structures of all sequences using Colabfold's batch mode.

We extracted the Rank 1 PDB structure for each sequence

And calculated TM-Scores

Results are examined using the scripts in the `notebooks` folder

 