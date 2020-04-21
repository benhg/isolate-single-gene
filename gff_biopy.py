from BCBio import GFF
from Bio import SeqIO

in_seq_file = "IPedibility.fasta"
in_seq_handle = open(in_seq_file)
seq_dict = SeqIO.to_dict(SeqIO.parse(in_seq_handle, "fasta"))
in_seq_handle.close()

with open("IPedibility_18S_guesses.fasta", "w") as fh:
    in_file = "raw_barrnap.gff3"
    in_handle = open(in_file)
    for rec in GFF.parse(in_handle, base_dict=seq_dict):
        taxon = rec.description
        sequence = str(rec.seq)
        guess_number = 1
        print(rec.description)
        for feature in rec.features:
            if feature.qualifiers["Name"][0] == "18S_rRNA":
                feature_loc = feature.location
                start = int(feature_loc._start)
                end = int(feature_loc._end)
                feature = sequence[start:end]
                fh.write(f">{taxon}, guess {guess_number}\n{feature}\n")
                guess_number += 1
                if guess_number == 3:
                    guess_number = 1


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--locations", type=str, help="Path to locations file in GFF3 format")
    parser.add_argument("--db", type=str, help="Path to database file in FASTA format")
    parser.add_argument("--out", type=str, help="Path to output file in FASTA format (needs not exist)")
    args = parser.parse_args()
    print(args)