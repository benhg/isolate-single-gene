# GFF Feature Extractor

## Introduction and Motivation

Looking around, it was surprisingly difficult to find a simple script for extracting features specified with a GFFv3 file. This is meant to be a dead-simple implementation of a CLI tool for extracting features from a database.

## Description

Given a FASTA formatted database of sequences and a GFFv3 file which contains features and their locations within sequences contained in the FASTA formatted database, this will extract the features and put them into a new FASTA file, with each entry titled the same way as the input, plus the name of the feature which was extracted. Here's an example. 

Input file:
```
>seq1
ACAGACTGCCGGTGATAAGCCGGAGGAAGGTGAGGATGACGTCAAGTCATCATGCCCCTTATGCCCTGGGCGACACACGTGCTACAATGGCCGGGACAAAGGGTCGCGATCCCGCGAGGGTGAGCTAACCCCAAAAACCCGTCCTCAGTTCGGATTGCAGGCTGCAACTCGCCTGCATGAAGCCGGAATCGCTAGTAATCGCCGGTCAGCCATACGGCGGTGAATTCGTTCCCGGGCCTTGTACACACCGCCCGTCACACTATGGGAGCTGGCCATGCCCGAAGTCGTTACCTTAACCGCAAGGAGGGGGATGCCGAAGGCAGGGCTAGTGACTGGAGTGAAGTCGTAACAAGGTAGCCGTACTGGAAGGTGCGGCTGGATCA
>seq2
ACAGACTGCCGGTGATAAGCCGGAGGAAGGTGAGGATGACGTCAAGTCATCATGCCCCTTATGCCCTGGGCGACACACGTGCTACAATGGCCGGGACAAAGGGTCGCGATCCCGCGAGGGTGAGCTAACCCCAAAAACCCGTCCTCAGTTCGGATTGCAGGCTGCAACTCGCCTGCATGAAGCCGGAATCGCTAGTAATCGCCGGTCAGCCATACGGCGGTGAATTCGTTCCCGGGCCTTGTACACACCGCCCGTCACACTATGGGAGCTGGCCATGCCCGAAGTCGTTACCTTAACCGCAAGGAGGGGGATGCCGAAGGCAGGGCTAGTGACTGGAGTGAAGTCGTAACAAGGTAGCCGTACTGGAAGGTGCGGCTGGATCA
```
Output File:
```
>seq1,18S_rRNA
GGGTCGCGATCCCGCGAGGGTGAGCTAACCC
>seq2,28S_rRNA
TAGTGACTGGAGTGAAGTCGTAACAAGGTAGCCGTA
```

## Usage

Simple, command-line based usage:
```
usage: gff_biopy.py [-h] --locations LOCATIONS --db DB --out OUT
                    [--filter FILTER]

required arguments:
  --locations LOCATIONS
                        Path to locations file in GFF3 format
  --db DB               Path to database file in FASTA format
  --out OUT             Path to output file in FASTA format (needs not exist)

optional arguments:
  -h, --help            show this help message and exit
  --filter FILTER       Name of type of feature to extract. Stored as a name
                        in the qualifiers section. Example: '18S_rRNA'
```