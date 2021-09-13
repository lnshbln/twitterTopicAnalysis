# -*- coding: utf-8 -*-
import os
import json
import pandas as pd
import csv
from sentimentAnalysis import sentimentAnalysis

def tweetBoxExtraction(lat_min,lon_min,lat_max,lon_max):
    tweetlist = []

    for k in range(6,8):
        for j in range(0,3):
            for i in range(1,9):
                try:
                    with open('distributedReader.2.1.twitterCrawler05.2019.0'+str(k)+'.'+str(j)+str(i)+'.bbox.json',encoding = "utf8", errors='ignore') as f: # replace the JSON file if needed
                        file = f.readlines() # read all the lines in the JSON file
                        for j in file:
                            # Remove extra lines separating each tweet in the json file
                            j = j.rstrip('\n'+',').rstrip().strip()

                            if j:
                                data = json.loads(j)  # Load the line into JSON format
                                # extract the fields needed
                                created_at = data["created_at"]
                                #tweet_utz = data["user"]["time_zone"]

                                user_id = data["user"]["id_str"]
                                tweets = data["text"]
                                if data["coordinates"] is not None:
                                    tweet_geo = data["coordinates"]["coordinates"]
                                    coord0 = tweet_geo[0]
                                    coord1 = tweet_geo[1]
                                    if float(lon_min)<=coord0<=float(lon_max):
                                        if float(lat_min)<=coord1<=float(lat_max):
                                            print(tweets)
                                    #tweetlist.append(tweets)
                                else:
                                    continue
                except IOError:
                    i+=1
                    continue

#tweetBoxExtraction(55.704502,37.512208,55.719927,37.574346)
#sentimentAnalysis('sentiment.txt','RedSquare.txt') #estimate the dominated emotions for a given territory
