# -*- coding: utf-8 -*-
import csv
import sys
from nltk.tokenize import word_tokenize
import re
import numpy as np


def sentimentAnalysis(vocabulary, inputFile):
    positive = []
    negative = []

    with open(vocabulary, encoding = "windows-1251", errors='ignore') as csv_file: #open vocabulary file

        csv_reader = csv.reader(csv_file, delimiter='\t')
        for row in csv_reader:
            positive.append(row[0])
            negative.append(row[1])

    sumpos = 0
    sumneg = 0
    text =[]
    with open(inputFile,encoding = "windows-1251", errors='ignore') as inputFile: #open input txt file with tweets
        fileReader = csv.reader(inputFile, delimiter='\t')

        for text in fileReader:
            for i in text:
                delpunctualtion = re.sub(r'[^\w\s]', '', i)
                lowstring = delpunctualtion.lower()
                text_tokens = word_tokenize(lowstring)
                tokens_pos = [word for word in text_tokens if word in positive]
                tokens_neg = [word for word in text_tokens if word in negative]
                if len(tokens_pos)>0:
                    sumpos += len(tokens_pos)

                if len(tokens_neg)>0:
                    sumneg += len(tokens_neg)
        if sumpos>sumneg:
            print("Positive")
        elif sumpos<sumneg:
            print("Negative")
        else:
            print("Neutral")


#sentimentAnalysis('/Volumes/Seagate Backup Plus Drive/PP/Summer/sentiment.txt','/Volumes/Seagate Backup Plus Drive/PP/POI/Moscow/Yakimanka.txt')

