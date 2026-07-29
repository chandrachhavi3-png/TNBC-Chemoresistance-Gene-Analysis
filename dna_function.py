# Core DNA analysis functions

def transcribe(sequence):
    rna=sequence.replace("T","U")
    return rna

def count_nucleotide(sequence):
    count_nucleotide={'A':0,'G':0,'T':0,'C':0}
    for base in sequence:
        count_nucleotide[base]=count_nucleotide[base]+1
    return count_nucleotide 

def GC_content(sequence):
    each_base=count_nucleotide(sequence)
    total_GC=each_base["G"]+ each_base['C']
    total_len=len(sequence)
    GC_content= (total_GC/total_len)*100
    return GC_content

def reverse_complement(sequence):
    complement_map={'A':'T','T':'A','G':'C','C':'G'}
    complement_seq=""
    for base in sequence:
        complement_seq = complement_seq + complement_map[base]
    result = complement_seq[::-1]
    return result

def read_fasta(filename):
    with open(filename,"r") as file:
        seq = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                continue
            seq = seq + line
    return seq 