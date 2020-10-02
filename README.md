# sentiment_hun
# Possibilities and limitations of a lexicon-based sentiment analysis of Hungarian political news 

Draft version


## Features

- Word Embedding with Word2vec model and parameters presented in the draft
- Sentiment dictionary: finds sentiment values based on given dictonary and corpus with the methods presented in the draft

## Usage

### Word Embedding

Run Word_embedding_w2v.py!
- Give the path of your folder containing all excel files of the embedding corpus!
- Give the column of the excels containing the text to embed on - NOTE: the name of this column must be identical in each excel!
- The Word2vec model is initialised with the parameters given in the draft!
- You have two options: 
	- One: Embedding of a list of positive and negative words - the result is an excel, containing all your embeddings
	- Two: Embedding of a single word and output a .txt


### Sentiment dictionary

Requirements: magyarlanc
	- Download ML_folder.jar from: [https://drive.google.com/file/d/1pPIldj6nTUbNk3HmCr_9XJn0WSHwMwdZ/view?usp=sharing]
	- Place ML_folder.jar into the output folder! 

Run MAIN_sentiment_dictionary.py!
- Input the excel name to analyse!
- Input the name of the column containing ids for the articles or a given text. Each row in the excel must have a unique id!
- Input the content column! The column composed of the main textual part of each excel row.
- Input the location of the dictonaries! Input the exact path where your dictionaries are located!
- Input the positive dictonary! The name of you .txt dictonary of positive words, each written seperately in a new line!
- Input the negative dictonary! The name of you .txt dictonary of negative words, each written seperately in a new line!
- You have two four ways to analyise:
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

The output is an excel file named "sentiment.xlsx" in the output folder along with a brief overview of choice of sentiment for each row of the desired excel.




The packages used in both programs belong to their rightful owners!
## Dependencies and credits:
 * [Gensim's Word2Vec] developed by Mikolow et al.
 * [pandas]
 * [magyarlanc]
 * [xlwt 1.3.0]
 * [NLTK's hungarian stoplist] (we use a modified version)
 




[Gensim's Word2Vec]: <https://radimrehurek.com/gensim/models/word2vec.html>
[pandas]: <https://pandas.pydata.org/>
[magyarlanc]: <https://rgai.inf.u-szeged.hu/magyarlanc>
[xlwt 1.3.0]: <https://pypi.org/project/xlwt/>
[NLTK's hungarian stoplist]: <https://www.nltk.org/>
[https://drive.google.com/file/d/1pPIldj6nTUbNk3HmCr_9XJn0WSHwMwdZ/view?usp=sharing]: <https://drive.google.com/file/d/1pPIldj6nTUbNk3HmCr_9XJn0WSHwMwdZ/view?usp=sharing>

