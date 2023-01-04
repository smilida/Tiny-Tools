## install proj4(required packages)
conda install -c conda-forge proj4

## install ggmsa(Use devtools or BiocManager)
# based on devtools
devtools::install_github("YuLab-SMU/ggmsa")
# based on BiocManager
BiocManager::install("ggmsa")

## Use ggmsa visualize MSA
library("ggmsa")
DNAMultipleAlignment <- Biostrings::readDNAMultipleAlignment("PATH/sample.fasta")
ggmsa(DNAMultipleAlignment, 164, 213, color='Chemistry_NT')
