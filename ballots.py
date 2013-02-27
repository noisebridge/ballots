#!/usr/bin/python

"Ballot generator for Noisebridge board elections"

__author__  = "Leif Ryge"
__license__ = "WTFPL 2012-2013 No Rights Reserved"

import sys, random, hashlib

def print_ballots( count, template, candidates, secret ):

    count      = int(count)
    template   = file(template).read().strip()
    candidates = file(candidates).read().strip().split('\n')
    secret     = file(secret).read().strip()
    ballots    = {}

    for i in range( count ):
        random.shuffle( candidates )
        ballot = "\n".join( "[ ] " + c for c in candidates )
        ballots[ hashlib.sha1(ballot+secret).hexdigest()[:6] ] = ballot

    for hash, ballot in ballots.items():
        print template % (hash, ballot)

if __name__ == "__main__":
    print_ballots( *sys.argv[1:] )

