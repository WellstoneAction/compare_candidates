import sys
from settings import *
import requests
import json
import operator
import twitter
from watson_developer_cloud import PersonalityInsightsV2 as PersonalityInsights 

def analyze(handle):

    #Invoking the Twitter API
    twitter_api = twitter.Api(consumer_key = consumer_key, consumer_secret=consumer_secret, access_token_key=access_token, access_token_secret=access_secret)

    #Retrieving the last 200 tweets from a candidate1
    statuses = twitter_api.GetUserTimeline(screen_name=handle, count=200, include_rts=False)

    #Putting all 200 tweets into one large string called "text"
    text = "" 
    for s in statuses:
        if (s.lang =='en'):
                text += s.text.encode('utf-8')

    #Analyzing the 200 tweets with the Watson PI API
    pi_result = PersonalityInsights(username=pi_username, password=pi_password).profile(text)

    #Returning the Watson PI API results
    return pi_result

#This function is used to flatten the result 
#from the Watson PI API
def flatten(orig):
    data = {}
    for c in orig['tree']['children']:
        if 'children' in c:
            for c2 in c['children']:
                if 'children' in c2:
                    for c3 in c2['children']:
                        if 'children' in c3:
                            for c4 in c3['children']:
                                if (c4['category'] == 'personality'):
                                    data[c4['id']] = c4['percentage']
                                    if 'children' not in c3:
                                        if (c3['category'] == 'personality'):
                                                data[c3['id']] = c3['percentage']
    return data


#This function is used to compare the results from
#the Watson PI API
def compare(dict1, dict2):
    compared_data = {}
    for keys in dict1:
            if dict1[keys] != dict2[keys]:
                compared_data[keys] = abs(dict1[keys] - dict2[keys])
    return compared_data


#The two Twitter handles
candidate1_handle = raw_input("What's the first candidate's Twitter handle? Don't include the '@' sign.: ")
candidate2_handle = raw_input("And the second candidate? ")


#Analyze the candidate1's tweets using the Watson PI API
candidate1_result = analyze(candidate1_handle)
candidate2_result = analyze(candidate2_handle)


#Flatten the results received from the Watson PI API
candidate1 = flatten(candidate1_result)
candidate2 = flatten(candidate2_result)

#Compare the results of the Watson PI API by calculating
#the distance between traits
compared_results = compare(candidate1,candidate2)

#Sort the results
sorted_results = sorted(compared_results.items(), key=operator.itemgetter(1))

print "Trait     |   Person1      |     Person2   |    Difference"
print "==========================================================="


#Print the results to the candidate1
for keys, value in sorted_results[:5]:
    print keys ,
    print (candidate1[keys]),
    print ('->'),
    print (candidate2[keys]),
    print ('->'),
    print (compared_results[keys])
