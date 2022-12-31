#!/bin/bash
# Author     : zhai1xiao
# Date       : 2022-05-06
# Function   : Convert ALL .aln files in a folder to .fasta files
# Instruction: sh aln2fasta_batch.sh PATH

dir=$1
ls $dir | while read line
do
	python3 aln2fasta.py ${dir}/${line}		
done
