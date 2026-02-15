DNA = "GCTA"
RNA = "CGAU"

def to_rna(dna_strand):
    return dna_strand.translate(str.maketrans(DNA, RNA))
