
from BCBio import GFF
from Bio import SeqIO

in_seq_file = "IPedibility.fasta"
in_seq_handle = open(in_seq_file)
seq_dict = SeqIO.to_dict(SeqIO.parse(in_seq_handle, "fasta"))
in_seq_handle.close()

in_file = "locations.gff3"
in_handle = open(in_file)
for rec in GFF.parse(in_handle, base_dict=seq_dict):
    print(rec)
in_handle.close()

