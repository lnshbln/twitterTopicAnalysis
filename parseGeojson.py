# -*- coding: utf-8 -*

import json
import ast


# importing the module
out_file = open("extractedCoordinates.txt", 'w') # open output file
for i in range(0,9):
    try:
        with open('distributedReader.2.1.twitterCrawler05.2019.06.2'+str(i)+'.bbox.json') as f: # replace "Your OWN JSON file.json" with your own JSON file
            file = f.readlines() # read all the lines in the JSON file
            for j in file:
                # Remove extra lines separating each tweet in the json file
                j = j.rstrip('\n'+',').rstrip().strip()  # j.rstrip('\n').rstrip().strip()
                 # k is recording the number of lines processed
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
                    else:
                        continue
                    out_file.write(str(created_at) + '\t'  + str(user_id) + '\t'+ str(coord1)+'\t'+ str(coord0)+'\t'  + '\n')

    except IOError:
        i+=1
        continue

