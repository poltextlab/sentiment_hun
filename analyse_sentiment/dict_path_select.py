#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""
The following function returns "path" variable based on user decision. 


'One: Simple' = After preprocessing use brute-force search to find words in positive and negative dictonaries. Each
token accounts for +1 or -1 respectively.


'Two': Simple with the addition of applying the "hungarian_2" stoplist 

'Three: Sentiment-score' = Use sentiment scoring after search.
                            -  sentiment_value: The result of the brute-force method search
                            -  ossz_sentiment = sum of all words with sentiment values
                            -  sentiment_threshold: ossz_sentiment / count of all tokens in an entry
                            -  sentiment_nullify: The ratio between negative and positive words in an entry
                        if sentiment_value < 0 and (sentiment_threshold > 0.1 or sentiment_nullify < 0.95 --> negative
                        if sentiment_value > 0 and (sentiment_threshold > 0.1 or sentiment_nullify < 0.95 --> postitive
                        if sentiment_threshold < 0.1 or sentiment_nullify > 0.95 --> neutral

'Four': Sentiment-score with the addition of applying the "hungarian_2" stoplist 

"""

def questions():    
    path = input('What would you like to do?'+"\n" 
                 'One: Simple'+"\n" 
                 'Two:' 'Simple + stopwords' + "\n"
                'Three: Sentiment-score'+"\n"
                 "Four: Sentiment-score + stopwords" + "\n") 
    
    return path

