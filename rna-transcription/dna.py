# def to_rna(dnastrand):
#     RNAcomplement = ""
#     for char in dnastrand:
#         if char == "G":
#             RNAcomplement += "C"
#         elif char == "C":
#             RNAcomplement += "G"
#         elif char == "T":
#             RNAcomplement += "A"
#         elif char == "A":
#             RNAcomplement += "U"
#     return RNAcomplement

def to_rna(dnastrand):

    DNAtoRNA = {'A': 'U',
            'C': 'G',
            'G': 'C',
            'T': 'A'}

    complement = ""
    for n in dnastrand:
        complement += DNAtoRNA[n]
    return complement
