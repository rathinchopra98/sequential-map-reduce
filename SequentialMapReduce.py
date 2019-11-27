import re
import timeit
from collections import Counter
from nltk.corpus import stopwords

startTime = timeit.default_timer()

data = open("DonaldTrumpTweets.txt", "r")

def no_stopwords(word):
    STOP_WORDS = set(stopwords.words('english'))
    return word not in STOP_WORDS and word and word.isalpha()

def filter_word(word):
    return re.sub(r'[^\w\s]','',word).lower()

def word_frequency(data):
    word_frequency = Counter()
    for text in data:
        text_tokens = text.split()
        text_tokens = map(filter_word, text_tokens)
        text_tokens = filter(no_stopwords, text_tokens)
        word_frequency.update(text_tokens)

    return word_frequency.most_common(10)

result = word_frequency(data)
for item in result:
    print (item)

elapsed_time = timeit.default_timer() - startTime
print ("Time Elapsed: " + str(elapsed_time))
