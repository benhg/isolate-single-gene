from BCBio import GFF
from Bio import SeqIO

in_seq_file = "IPedibility.fasta"
in_seq_handle = open(in_seq_file)
seq_dict = SeqIO.to_dict(SeqIO.parse(in_seq_handle, "fasta"))
in_seq_handle.close()

in_file = "raw_barrnap.gff3"
in_handle = open(in_file)
for rec in GFF.parse(in_handle, base_dict=seq_dict):
    sequence = rec.seq
    taxon = rec.id
    # print(rec)
    print(rec.description)
    for feature in rec.features:
    	print(feature["qualifiers"]["Name"])

#in_gff = GFF.parse(in_handle, base_dict=seq_dict)

