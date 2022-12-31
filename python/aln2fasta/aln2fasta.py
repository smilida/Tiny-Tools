# Author  : zhai1xiao
# Date    : 2022-05-06
# Function: Convert .aln format to .fasta/.fas format

import sys, os

def aln2fasta(file_path: str, result_name: str):
    """
    read .aln file

    Args:
        file_path: PATH
        result_name: result file name

    """
    identifiers = []
    sequences = []
    with open(file_path, 'r') as fin:
        for line in fin:
            if len(line.split()) > 0:
                id = line.split()[0]
                seq = line.split()[1]
                if id not in identifiers:
                    identifiers.append(id)
                    sequences.append(seq)
                else:
                    index = identifiers.index(id)
                    sequences[index] = sequences[index] + seq
    
    with open(result_name, "w") as fout:
        for i in range(len(identifiers)):
            fout.write(">" + identifiers[i] + "\n")
            fout.write(sequences[i])
            fout.write("\n")

if __name__ == '__main__':
    file_path = sys.argv[1]
    result_name = file_path + ".fasta"
    os.system("tail -n +3 " + file_path + " | sed -e '/*/d;/:/d;/\./d' | sed '/^$/d' > tmp.aln")
    aln2fasta("tmp.aln", result_name)
    os.system("rm tmp.aln")
