import urllib
import simplejson

#ref: https://dev.twitter.com/docs/api/1.1/get/search/tweets

def searchTweets(query):
 search = urllib.urlopen("http://search.twitter.com/search.json?q="+query)
 dict = simplejson.loads(search.read())
 for result in dict["results"]: # result is a list of dictionaries
  print "*",result["text"],"\n"

# we will search tweets about "fc liverpool" football team
searchTweets("fc+liverpool")
