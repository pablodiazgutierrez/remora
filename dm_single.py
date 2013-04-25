#!/usr/bin/env python
'Script to send a direct message to a specific user, by screen_name'

import pmtwitter, sys

if __name__ == '__main__':
    if len(sys.argv)<3:
        print "Usage: dm_single.py screen_name 'message'"
        sys.exit(-1)
    params = sys.argv[1:]
    sn = params[0]
    message = params[1]
    
    pmtwitter.api.PostDirectMessage(sn, message)
