
# Source http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0085733#s3

import askdb
from askutils import Friend
from facepy import GraphAPI

# Quick and dirty authentication - Get a USER access_token from facebook
# Go to: https://developers.facebook.com/tools/explorer 
# Copy/paste token below
ACCESS_TOKEN = 'CAACEdEose0cBADXxAL00y7l8LdfQCXs2NpOYxlvtJGHrVgXZCkWrlKSP0TGgbxBBGiBr7cLkQCZC29Jt29GNODJc2Ec7UOUMNepIuvtDnCjQNaDV6iBekZCEydX76IfOKm3pAMRbnSlBGJeookuRVn3ezbcyOhuHwVYg5ur2ZAtLKRJQq4T9B9303Ja5fvwi1TIMIZAmvuTUaZANF2GMZArmHtwDDBFKKsZD'

# Create FB Graph object and get friends statuses
# *** NEED TO HANDLE PAGINATION ***
graph = GraphAPI(ACCESS_TOKEN)
#data_generator = graph.get('me?fields=friends.limit(10){statuses.limit(10){message},name}',page=True)
data_generator = graph.get('me?fields=friends{statuses{message},name}',page=True)

fs = []
for data in data_generator:
    #a = graph.get('me?fields=friends{statuses{message}}')

    # okay lets get this in a form that I can work with ie-> fs = {"NAME": {"statuses": [status]}}
    friends = data['friends']['data'] #list... oh lets loop over to build a simplified dict
    for friend in friends:
        name = friend['name']
        statuses = []
        if 'statuses' in friend:
            for status in friend['statuses']['data']: # another list :-(
                if 'message' in status:
                    statuses.append(status['message'])
        fs.append(Friend(name, statuses))

# Reporting Section
print """********************************************************************
* Disclamier: This is only a proof of concept and the results here *
* do NOT reflect true depression or suicidal thinking              *
********************************************************************""" 

print """
===============================================================
=                             Ask..                           =
=              Are your friends okay? Why not ask?            =
= The higher the rating the more negative your friend's posts =
==============================================================="""
print " Name      Rating"
for r in fs:
    print "%s   %s" % (r.name, r.rating)
