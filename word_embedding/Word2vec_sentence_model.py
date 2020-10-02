#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
Importing gensim's Word2vec model and 
Importing our edited stopword list based on NLTK's hungarian list
"""

from gensim.models import word2vec

import gensim, os, nltk

import pandas as pd
stopwords = open('hungarian_2', encoding='utf-8')
stop_words = stopwords.read().split()
import re
import glob


# In[2]:


"""
Mondat model class will set the parametes of the embedding (for detailed information on the exact parameters of the model see the draft!) and the file(s) to embed on!
"""

class mondat_model:
    
    def __init__(self):
        
        
        self.excel_hely = input('Give the path of your folder containing all excel files of the embedding corpus!')
        self.excel_content = input('Give the column of the excels containing the text to embed on - NOTE: the name of this column must be identical in each excel!')
        print('Processing. Please Wait!')
        self.wv = self.word2vec_model()
        

    
    class word2vec_model:

        def __init__(self):

            self.min_count = 5
            self.window = 3
            self.negative = True
            self.iter = 10

        

word2vec_model_mondat = mondat_model()


# In[4]:


"""
Processing of the embedding corpus/corpora
"""

def import_excel():
    listofwords = []
    cikk = []
    szavak = []
    mondat = []
    mondatok = []
    os.chdir(word2vec_model_mondat.excel_hely)
    for i in os.listdir(os.getcwd()): 
        file_nev = str(i)
        text = pd.read_excel(file_nev)      
        sorok = text[str(word2vec_model_mondat.excel_content)].to_list()
        for sor in sorok:
            if (type(sor) != float and len(sor)>1):
                s = sor.split(" ")                       #### Tokenizing each each row of the excel
                listofwords.append(s)
                for n in listofwords:
                    n.append('END_OF_ARTICLE')                #### Appending END_OF_ARTICLE string to the end of each entry that will singal the end of the article for processing
                for szo in s:
                    if (type(szo) != float) and (len(szo)>1):
                        if szo.endswith('!') or szo.endswith('?') or szo.endswith('.'): ### Removing punctuation and seperating by sentences
                            punctuaction = re.compile(r'[,!.˙)(?:"";]') 
                            szo = re.sub(punctuaction,'',szo)
                            szo = szo.lower()
                            if szo not in stop_words: ### Filtering out stopwords
                                szavak.append(szo)
                                mondat.append(szavak)
                                szavak = []

                        else:
                            punctuaction = re.compile(r'[,!.˙)(?:"";]')
                            szo = re.sub(punctuaction,'',szo)
                            szo = szo.lower()
                            if (szo != 'END_OF_ARTICLE') and (szo not in stop_words):
                                szavak.append(szo)
                            if szo == 'END_OF_ARTICLE':
                                cikk.append(szavak)
                                szavak = []
    return mondat


def main():
    import_excel()

if __name__ == "__main__":
    main()

