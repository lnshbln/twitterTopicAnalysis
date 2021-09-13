# -*- coding: utf-8 -*-
import pandas as pd
import os
import json
import ast
import re
from collections import Counter
from nltk.corpus import stopwords
import nltk
import ssl
from wordcloud import WordCloud
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
import seaborn as sns
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
import nltk
nltk.download('wordnet')
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from gensim import corpora, models
'''
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
'''

nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import word_tokenize



def LDA (): #calculate LDA model

    tweetlist = []
    dataset =[]

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
                                    tweetlist.append(lowstring)

                                else:
                                    continue
                except IOError:
                    i+=1
                    continue



    wordlist =[]

    all_stopwords = stopwords.words('russian')
    eng_stopwords = stopwords.words('english')
    all_stopwords.append('обо')
    all_stopwords.append('ок')
    spb = ['санкт','петербург', 'питер', 'спб', 'северная', 'столица', 'город','неве','белых', 'ночей','культурная','россии','окно','европу','град','петров','петрополь','пальмира','венеция','невоград','ленина','герой','революций','spb','st','petersburg','sankt','saint','leningrad','petrograd','europe','peter','saintpetersburg','sanktpetersburg','sanktpeterburg','санктпетербург','ленинград','санктпетербурге',"санктпетербургу","нева"]
    moscow = ['москва','рим','первопрестольная','нерезиновая','златоглавая','деревня','белокаменная','дефолт','сити','мск','moskva','moscow','msk','msc','москвы','москвой','москву','московский']
    for i in eng_stopwords:
        all_stopwords.append(i)
    for i in spb:
        all_stopwords.append(i)
    for i in moscow:
        all_stopwords.append(i)
    for text in tweetlist:
        text_tokens = word_tokenize(text)
        tokens_without_sw = [word for word in text_tokens if not word in all_stopwords]
        for i in tokens_without_sw:
            if len(i)>3:
                try:
                    if int(i):
                        continue
                except ValueError:
                    wordlist.append(i)
            else:
                continue

    from nltk.stem.snowball import SnowballStemmer

    # Create p_stemmer of class PorterStemmer
    stemmer = SnowballStemmer("russian")
    texts = [stemmer.stem(i) for i in wordlist]

    stemmer_en = SnowballStemmer("english")
    texts_conv = [stemmer_en.stem(i) for i in texts]

    #print (texts_conv)

    dictionary = corpora.Dictionary([texts_conv])

    # convert tokenized documents into a document-term matrix
    corpus = [dictionary.doc2bow(text) for text in texts_conv]

    # generate LDA model
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=20, id2word=dictionary, passes=20)

LDA()
