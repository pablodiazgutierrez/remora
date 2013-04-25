#!/usr/bin/env python
'Script to send a direct message to a number of followers, making sure we are not repeating users'

import pmtwitter, sys

if __name__ == '__main__':
    if len(sys.argv)<3:
        print "Usage: dm.py num_users 'message'"
        sys.exit(-1)
    params = sys.argv[1:]
    num_users = int(params[0])
    message = params[1]
    burn_file = 'burn_file'
    print 'Direct-messaging %d users, controlling with file %s and content "%s"' % (num_users, burn_file, message)

    users = []
    with open(burn_file) as f:
        users = f.readlines()
        users = [u.strip() for u in users if u.strip()]
        #print len(users), "users already burned:", users
        
        followers = pmtwitter.api.GetFollowers()
        print len(followers), 'followers'

        n = 0
        for ff in followers:
            sn = ff.screen_name
            if sn not in users:
                n += 1
                print n, 'sending direct message to', sn
                pmtwitter.api.PostDirectMessage(sn, message)
                #print 'pmtwitter.api.PostDirectMessage(%s, %s)' % (sn, message)
                users.append(sn)
                if n>=num_users:
                    break
            else:
                print sn, 'already burned; skipping'
        print n, 'direct messages sent'

    with open(burn_file, "w") as f:
        for u in users:
            f.write("%s\n" % u)
