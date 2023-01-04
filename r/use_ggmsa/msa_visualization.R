## Use ggmsa visualize MSA
library("ggmsa")
DNAMultipleAlignment <- Biostrings::readDNAMultipleAlignment("PATH/sample.fasta")
ggmsa(DNAMultipleAlignment, 164, 213, color='Chemistry_NT')
