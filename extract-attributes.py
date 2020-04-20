#!/usr/bin/env python

import sys
import os

for line in sys.stdin:
    convertedLine = ""
    chomped_line = line.rstrip(os.linesep)
    if chomped_line.startswith('##'):
        pass
    elif chomped_line.startswith('track'):
        # skip non-standard use of track keyword by Ensembl 
        pass
    else:
        elems = chomped_line.split('\t')
        cols = dict()
        try:
            cols['seqname'] = elems[0].lstrip(' ') # strip leading whitespace
            cols['source'] = elems[1]
            cols['feature'] = elems[2]
            cols['start'] = int(elems[3])
            cols['end'] = int(elems[4])
            cols['score'] = elems[5]
            cols['strand'] = elems[6]
            cols['frame'] = elems[7]
            cols['attributes'] = elems[8].rstrip(' ') # strip trailing whitespace
        except IndexError as ie:
            sys.stderr.write("[%s] - Error: Input appears to be missing GTF-specific fields (check that your input data is GTF-formatted)\n" % (sys.argv[0]))
            sys.exit(os.EX_DATAERR)

        try:
            cols['comments'] = elems[9]
        except IndexError as ie:
            cols['comments'] = None

        attributes = dict(item.strip().split(' ') for item in cols['attributes'].split(';') if item)
