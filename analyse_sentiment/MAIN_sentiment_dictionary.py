#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import re
import pandas as pd
import numpy as np
import re
import sys
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# In[2]:


"""
Importing Excel_to_txt.py: Takes the given excel file - stored in the object variable answer.excel_name - zips the given
excel indexes to the excel column containing the given main content of the file and writes each row into a seperarte .txt
"""


import Excel_to_txt


# In[3]:


"""
Runing magyarlanc from cmd -  magyarlanc aims at the basic linguistic processing of Hungarian texts. 
The toolkit consists of only JAVA modules (there are no wrappers for other programming languages), which guarantees 
its platform independency and its ability to be integrated into bigger systems (e.g. web servers). - from https://rgai.inf.u-szeged.hu/magyarlanc
"""


# In[4]:


os.system('cmd /c "java -jar ML_folder.jar .\"')


# In[5]:


os.chdir('..')


# In[6]:


"""
Importing our edited stopword list based on NLTK's hungarian list
"""


# In[7]:


stopwords = open('hungarian_2.txt', encoding='utf-8')
stop_words = stopwords.read().split()


# In[8]:


"""
Importing questions from dict_path_select.py. This gives the user the option to select the way
in which the program utilises semtiment analysis.

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


# In[11]:


from dict_path_select import questions
from user_options import answer
os.chdir(answer.base_dir)
df = pd.read_excel(answer.excel_name+'.xlsx')



def processing(path):
    
    
 
        szotar_neg_clean = []
        szotar_poz_clean = []
        lemma_list = []
        lemma_list_poz = []
        lemma_list_temp = []
        lemma_list_neg = []
        lemma_count_cikk = []



        os.chdir(answer.dict_loc)

        """
        Initiating given dictonaries
        """

        szotar_poz = open(answer.dict_name_pos+'.txt', 'r', encoding='utf-8')
        szotar_neg = open(answer.dict_name_neg+'.txt', 'r', encoding='utf-8')



            
        def process_dict(szotar):
            szotar_clean = []
            for w in szotar: 
                w = w.strip('\n')
                szotar_clean.append(w.lower())
            return szotar_clean

        szotar_neg_clean = process_dict(szotar_neg)
        szotar_poz_clean = process_dict(szotar_poz)


        os.chdir(answer.base_dir)
        os.chdir('.\output')

        """
        Reading all lemmatized files from the output folder and reseting count and sentiment_value
        """
        
        
        for filename in os.listdir(os.getcwd()):
            sentiment_value = 0
            count = 0
            if filename.endswith('.txt') or filename == 'ML_folder.jar':
                continue
            with open(filename, 'r', encoding='utf-8') as file:
                file_list = file.readlines()

            """
            Removing punctuation and counting the number of tokens in an entry.
            """
    

                
                
            
            
            lemma_count_cikk = []
            for e in file_list:
                sor = re.split(r'\t+', e)
                if sor[0] != '\n':
                    lemma = (sor[1])
                    punctuaction = re.compile(r'[,!.˙)(?:”"";]')
                    lemma = re.sub(punctuaction,'',lemma)
                    if path == "Two" or path == "Four":                ### Removing stopwords based on choice of user
                        if len(lemma) > 0 and lemma not in stop_words:
                            lemma_count_cikk.append(lemma)
                            count = count + 1
                    if path == "One" or path == "Three":
                        if len(lemma) > 0:
                            lemma_count_cikk.append(lemma)
                            count = count + 1 



            for n in file_list:
                sor = re.split(r'\t+', n)
                if len(sor[0]) > 1:
                    lemma = (sor[1])
                    lemma_list_temp.append(lemma)
                    
                    
                    """
                    Checking whether lemma is in positive or negative dictonary. If in positive, add one to the sentiment value 
                    of the article, if in negative add minus one to the sentiment value
                    """



                    if (lemma_list_temp[0] in szotar_poz_clean):
                        sentiment_value += 1
                        print(lemma, 'pozitív')
                        lemma_list.append(lemma + ' ' + 'pozitív')
                        lemma_list_poz.append(lemma)
                    if (lemma_list_temp[0] in szotar_neg_clean):
                        sentiment_value -= 1
                        print(lemma, 'negatív')
                        lemma_list.append(lemma + ' ' + 'negatív')
                        lemma_list_neg.append(lemma)

                    lemma_list_temp = []
                    
                    
                    
            """
            If "path" variable from dict_path_select.py is One: Each
            token accounts for +1 or -1 respectively. The result of this part is a .txt, which contains the details of 
            sentiment analysis. 
            """

            if path == 'One' or path == 'Two':
               
                


                if filename.endswith('.out'):          
                    with open(str(filename+'_sentiment.txt'), 'w') as file:
                            file.writelines([str('\n'.join(lemma_list)) + "\n", 
                                             'Number of positive words: ' + str((len(lemma_list_poz))) + "\n", 
                                             'Number of negative words: ' + str((len(lemma_list_neg))) + "\n", 
                                             'Sentiment value sum: ' + str(sentiment_value)])



                    filename = str(filename).replace('.txt', '')
                    filename = str(filename).replace('.out', '')
                    row_indexes = df[answer.excel_column] == str(filename)


                    if sentiment_value < 0:
                        df.loc[row_indexes, 'sentiment']='negative' 
                    if sentiment_value > 0:
                        df.loc[row_indexes, 'sentiment']='positive' 
                    if sentiment_value == 0:
                        df.loc[row_indexes, 'sentiment']='neutral' 

                    
                    """
                    The following excel is created, which contains the estimated sentiment value of all the articles given in the input 
                    excel.
                    """
                    
                    
                    df.to_excel('sentiment.xlsx')


                    lemma_list = []
                    lemma_list_neg = []
                    lemma_list_poz = []

                    """
                    If "path" variable from dict_path_select.py is Two: Sentiment-score' = Use sentiment scoring after search.
                                        -  sentiment_value: The result of the brute-force method search
                                        -  sentiment_sum = sum of all words with sentiment values
                                        -  sentiment_threshold: ossz_sentiment / count of all tokens in an entry
                                        -  sentiment_nullify: The ratio between negative and positive words in an entry
                                    if sentiment_value < 0 and (sentiment_threshold > 0.1 or sentiment_nullify < 0.95 --> negative
                                    if sentiment_value > 0 and (sentiment_threshold > 0.1 or sentiment_nullify < 0.95 --> postitive
                                    if sentiment_threshold < 0.1 or sentiment_nullify > 0.95 --> neutral. 
                    """



            if path == 'Three' or path == 'Four':

                if count is 0:
                    count = 1

                ossz_sentiment = (len(lemma_list_poz)) + (len(lemma_list_neg))
                sentiment_threshold = ossz_sentiment / count


                if len(lemma_list_neg) is 0:
                    lemma_list_neg.append('EMPTY_LIST')
                if len(lemma_list_poz) is 0:
                    lemma_list_poz.append('EMPTY_LIST')


                max_sentiment = max(len(lemma_list_poz), len(lemma_list_neg))
                min_sentiment = min(len(lemma_list_poz), len(lemma_list_neg))
                sentiment_nullify = min_sentiment / max_sentiment


               


                if filename.endswith('.out'):          
                    with open(str(filename+'_sentiment.txt'), 'w') as file:
                            file.writelines([str('\n'.join(lemma_list)) + "\n", 
                                             'Number of positive words: ' + str((len(lemma_list_poz))) + "\n", 
                                             'Number of negative words: ' + str((len(lemma_list_neg))) + "\n", 
                                             'Sentiment_nullify_score: ' + str(sentiment_nullify) + "\n",
                                             'Sentiment_threshold: ' + str(sentiment_threshold) + "\n",
                                             'Sentiment value sum:' + str(sentiment_value) + "\n",
                                                'Sum of tokens: ' + str(count)]) 




                    filename = str(filename).replace('.txt', '')
                    filename = str(filename).replace('.out', '')
                    row_indexes = df[answer.excel_column] == str(filename)


                    if sentiment_value < 0 and (sentiment_threshold > 0.1 or sentiment_nullify < 0.95):
                        df.loc[row_indexes, 'sentiment']='negative'
                    if sentiment_value > 0 and (sentiment_threshold > 0.1 or sentiment_nullify < 0.95):
                        df.loc[row_indexes, 'sentiment']='pozitive' 
                    if sentiment_threshold < 0.1 or sentiment_nullify > 0.95:
                        df.loc[row_indexes, 'sentiment']='neutral'


                    df.to_excel('sentiment.xlsx')


                    lemma_list = []
                    lemma_list_neg = []
                    lemma_list_poz = []

    




def main():
    path = questions()
    processing(path)

    
if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




