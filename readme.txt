Packages used:
-csv
-operator
-time
-pyproj
-math
-pandas
-os
-json
-ast
-re
-collections
-nltk
-ssl
-wordcloud
-sklearn
-numpy
-seaborn
-gensim
-sentimentAnalysis
-sys

1. To calculate LDA model, place the script "LDA.py" to the folder with .json files. Double check the number of collector and a time period.

2. To make keyword analysis, place the keyword vocabulary path as an input file, place the script "keywordsearch.py" to the folder with .json files. Double check the number of collector and a time period.

3. To extract tweets from territory of interest, set the lower left and higher right coordinates of a box. Place the script "tweetBoxExtraction.py" to the folder with .json files. Double check the number of collector and a time period.

4. To estimate the dominated emotions for a given territory use "sentimentAnalysis.py". Set the path to the emotions vocabulary and a .txt file for analysis.


Optional:
The original idea of using iterative clustering failed, as it turned out that the position of the centroid would change every time, 
since it depends on the average distance, which would change when some points were excluded. 
There was also an idea to use Agglomerative Hierarchical Clustering, but its use also turned out to be inapplicable in this work due to 
its work on the basis of the frequency of occurrence of points, while some areas contained a small number of tweets.

The scripts "parseGeojson.py","coordTransform.py", "sortFile.py", "euclidianDist.py" were used to test the initial hypothesis. 
1. Place the script "parseGeojson.py" to the folder with .json files. Double check the number of collector and a time period.
2. Transform LatLon coordinates to XY using "coordTransform.py". Set the path to input and output .txt files.
3. The resulted file should be sorted using "sortFile.py". Set the path to input and output .txt files.
4. Calculate the median euclidian distance for all pair of coordinates



