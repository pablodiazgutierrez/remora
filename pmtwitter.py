#!/usr/bin/env python
'Script to send a direct message to a number of followers, making sure we are not repeating users'

import twitter
import simplejson
import urllib
import sys

# Log in with user productivity151 and app 'remora'
consumer_key = 'mykey'
consumer_secret = 'mysecret'
access_token_key = 'mytokenkey'
access_token_secret = 'mytokensecret'
api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_token_key, access_token_secret=access_token_secret)
#print api.VerifyCredentials()

def search(query, rpp=10, log=False):
    '''
    query: the search term
    rpp: results per page
    '''
    url = "http://search.twitter.com/search.json?rpp=%d&q=%s" % (rpp,query)
    result = urllib.urlopen(url)
    dict = simplejson.loads(result.read())
    try:
        if log:
            for item in dict["results"]: # result is a list of dictionaries
               print "%s:\t'%s'" % (item["from_user"],item["text"])
    except Exception, err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        pass
        
    return dict

def quotes(query, rpp=15):
    try:
        dict = search(query, rpp)
        result = ["%s:\t'%s'" % (item["from_user"],item["text"]) for item in dict["results"]]
        return result
    except Exception, err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        pass
    return []

def people(query, rpp=15):
    try:
        dict = search(query, rpp)
        ids = [item["from_user"] for item in dict["results"]]
        unique = set(ids)
        return unique
    except Exception, err:
        sys.stderr.write('ERROR: %s\n' % str(err))
        pass
    return []

