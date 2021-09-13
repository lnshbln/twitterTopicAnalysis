# -*- coding: utf-8 -*-
import json
import re
import csv

def keywordSearch(vocabulary):

    Tourism = []
    Emotion = []
    Health = []
    Photo = []
    Wishes = []
    Places = []
    Items = []

    with open(vocabulary, encoding = "windows-1251", errors='ignore') as csv_file: #open vocabulary file

        csv_reader = csv.reader(csv_file, delimiter='\t')
        for row in csv_reader:
            Tourism.append(row[0])
            Emotion.append(row[1])
            Health.append(row[2])
            Photo.append(row[3])
            Wishes.append(row[4])
            Places.append(row[5])
            Items.append(row[6])
    tweetlist = []
    dataset =[]
    a = 0
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
                                user_id = data["user"]["id_str"]
                                tweets = data["text"]
                                if data["coordinates"] is not None:
                                    tweet_geo = data["coordinates"]["coordinates"]
                                    coord0 = tweet_geo[0]
                                    coord1 = tweet_geo[1]
                                    delpunctualtion = re.sub(r'[^\w\s]', '', tweets)
                                    lowstring = delpunctualtion.lower()
                                    if a ==lowstring:
                                        print(a, lowstring)
                                        continue
                                    else:
                                        tweetlist.append(lowstring)
                                        a = lowstring

                                else:
                                    continue
                except IOError:
                    i+=1
                    continue


    tweetlist_cleared =[]
    for i in tweetlist:
        if len(i)<3:
            continue
        else:
            tweetlist_cleared.append(i)

    countT= 0
    countE= 0
    countH= 0
    countP= 0
    countW = 0
    countPl = 0
    countI = 0
    for i in tweetlist_cleared:
        for j in i:
            for k in Tourism:
                if j == k:
                    countT += 1
        if countT>0:
            print (countT)
        else:
            print("No objects found in Tourism")

            for k in Emotion:
                if j == k:
                    countE += 1
        if countE>0:
            print (countE)
        else:
            print("No objects found in Emotions")

            for k in Health:
                if j == k:
                    countH += 1
        if countH>0:
            print (countH)
        else:
            print("No objects found in Health")

            for k in Photo:
                if j == k:
                    countP += 1
        if countP>0:
            print (countP)
        else:
            print("No objects found in Photo")

            for k in Wishes:
                if j == k:
                    countW += 1
        if countW>0:
            print (countW)
        else:
            print("No objects found in Wishes")

            for k in Places:
                if j == k:
                    countPl += 1
        if countPl>0:
            print (countPl)
        else:
            print("No objects found in Places")

            for k in Items:
                if j == k:
                    countI += 1
        if countI>0:
            print (countI)
        else:
            print("No objects found in Items")


keywordSearch('keywordVocabulary.txt') #set the vocabulary
