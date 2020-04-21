from BCBio import GFF
from Bio import SeqIO



def extract(in_db, locations, out_file):

    in_seq_handle = open(in_db)
    seq_dict = SeqIO.to_dict(SeqIO.parse(in_seq_handle, "fasta"))
    in_seq_handle.close()

    with open(out_file, "w") as fh:
        in_handle = open(locations)
        for rec in GFF.parse(in_handle, base_dict=seq_dict):
            taxon = rec.description
            sequence = str(rec.seq)
            for feature in rec.features:
                if feature.qualifiers["Name"][0] == "18S_rRNA":
                    feature_loc = feature.location
                    start = int(feature_loc._start)
                    end = int(feature_loc._end)
                    feature = sequence[start:end]
                    fh.write(f">{taxon}, guess {guess_number}\n{feature}\n")


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--locations", type=str, help="Path to locations file in GFF3 format")
    parser.add_argument("--db", type=str, help="Path to database file in FASTA format")
    parser.add_argument("--out", type=str, help="Path to output file in FASTA format (needs not exist)")
    args = parser.parse_args()
    print(args)