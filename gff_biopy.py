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
    guess_number = 0
    print(rec.description)
    for feature in rec.features:
        if feature.qualifiers["Name"][0] == "18S_rRNA":
            feature_loc = feature.location
            start = feature_loc._start
            end = feature_loc._end
            print(type(start))
            guess_number += 1
            if guess_number == 2:
                guess_number = 0

#in_gff = GFF.parse(in_handle, base_dict=seq_dict)

