#!/usr/bin/env python

import pmtwitter
import sys

if __name__ == '__main__':
    params = sys.argv[1:]
    if len(params)==0:
        print "Usage: remora.py <search1 search2 search3...>"

    for query in params:
        crowd = pmtwitter.people(query, 10)
        print query, "has these", len(crowd), "results:"
        for who in crowd:
            print "Befriending:",who
            pmtwitter.api.CreateFriendship(who)

#        gossip = quotes(query)
#        print "gossip:", gossip
#        for said in gossip:
#            print said
