#!/usr/bin/python

"Ballot generator for Noisebridge board elections"

__author__  = "Leif Ryge"
__license__ = "WTFPL 2012-2013 No Rights Reserved"

import sys, random, hashlib, hmac

def print_ballots( count, template, candidates, secret ):

    count      = int(count)
    template   = file(template).read().strip()
    candidates = file(candidates).read().strip().split('\n')
    secret     = file(secret).read().strip()
    ballots    = {}

    for i in range( count ):
        random.shuffle( candidates )
        ballot = "\n".join( "[ ] " + c for c in candidates )
        key = hmac.new(secret, msg=ballot, digestmod=hashlib.sha1).digest().encode("base64")
        ballots[key] = ballot

    for hash, ballot in ballots.items():
        print template % (hash, ballot)

if __name__ == "__main__":
    if len(sys.argv[1:]) != 4:
        print "Usage: %s <count> <ballot_template> <candidates_file> <secret_file>" % sys.argv[0]
        sys.exit(1)
    print_ballots( *sys.argv[1:] )
