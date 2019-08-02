'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Get the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()
# Continue your program below!
#Create list of tweets
Subjectivity = []
Polarity = []
# Textblob sample:
for t in tweetData:
    tb = TextBlob(t['text'])
    #Add to Subjectivity and Polarity list
    Polarity.append(tb.polarity)
    Subjectivity.append(tb.subjectivity)


#find average
sum1 = 0
sum2 = 0
for p in Polarity:
    sum1 += p
    dif1 = sum1/len(Polarity)

for s in Subjectivity:
    sum2 += s
    dif2 = sum2/len(Subjectivity)

#create an empty string called alltweets using two quotes
alltweets = ""
for tweets in tweetData:
    alltweets += t['text']
print(alltweets)

tb_tweets = TextBlob(alltweets)
filteredWords = []
#filter out words you want into the empty list above
nofilter = ['and','like','about','the','http','for','https','then','t.co/QFTaOcOpxDIf','because']
for word in tb_tweets.words:
            if len(word)< 3:
                continue
            elif word in nofilter:
                continue
            elif word.isnumeric():
                continue
            else:
                filteredWords.append(word)
print(filteredWords)

word_counts = {}

for term in filteredWords:
    if term in word_counts:
        continue
    else:
        count = tb_tweets.word_counts[term]
        word_counts[term] = count

wordcloud = WordCloud().generate_from_frequencies(word_counts)
plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
