## install ggmsa(Use devtools or BiocManager)
# based on devtools
devtools::install_github("YuLab-SMU/ggmsa")
# based on BiocManager
BiocManager::install("ggmsa")

## Use ggmsa
library(ggmsa)
protein_sequences <- system.file("extdata", "sample.fasta", package = "ggmsa")
ggmsa(protein_sequences, start = 221, end = 280, char_width = 0.5, seq_name = TRUE) + geom_seqlogo() + geom_msaBar()
