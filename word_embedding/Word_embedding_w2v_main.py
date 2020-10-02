#!/usr/bin/env python
# coding: utf-8

# In[1]:


from gensim.models import word2vec


# In[2]:


import gensim, os
import pandas as pd

"""
Importing our edited stopword list based on NLTK's hungarian list
"""

stopwords = open('hungarian_2.txt', encoding='utf-8')
stop_words = stopwords.read().split()



import re
import glob
import xlwt 
from xlwt import Workbook

"""
Importing Word2vec_sentence_model.py 
"""


from Word2vec_sentence_model import word2vec_model_mondat, mondat_model 
from Word2vec_sentence_model import import_excel


# In[3]:


mondat_modell = import_excel()


# """""" Importing Word2vec_sentence_model.py

# In[4]:


"""
Printing word2vec parameters for when the program is ran from the command line
"""


# In[5]:


print('Building word2vec model: Params: Min_count = 5, window = 3, negative_sampling, iter = 10')


# In[6]:


word2vec_model_mondat = gensim.models.Word2Vec(mondat_modell, sg=1, 
                                        min_count=5,
                                        window = 3, negative=True, iter=10)


# In[7]:


print('Model ready!')


# In[8]:


question = input('What would you like to do' + "\n" 
                 'One: Embedding of a list of positive and negative words' + "\n"
                 'Two: Embedding of a single word')


# In[9]:


if question == 'One':
    cwd = str(os.getcwd())
    def posizive_list():    
        word_embedding_pos_loc = input('Give to location of the list of positive words to embed!') 
        word_embedding_pos = input('Give the name of the positive list!')
        error_words_poz = []
        wb = Workbook()
        sheet1 = wb.add_sheet('Word_embedding_pos')   ### Creating an excel for the results
        os.chdir(word_embedding_pos_loc)
        
        """
        Opening given positive list of words and using word2vec_mondat_model to embed each word, which yields the top 100 closest words
        """
        
        pos_list = open(word_embedding_pos+'.txt', encoding='utf-8')   
        pos_list_2 = pos_list.read().split()
        rows = 0
        columns = 0
        for word in pos_list_2:
            columns = columns + 1
            try:
                embedding_i = word2vec_model_mondat.wv.most_similar(word, topn=100)
                sheet1.write(int(rows), int(columns), str(word+' '+'positive'))
                n = 0
                for v in embedding_i:
                    rows = rows + 1
                    n = n + 1
                    sheet1.write(int(rows),int(columns), str(v))
                    if n == 100:
                        rows = 0
                        wb.save('embedding_pos.xls') 


            except: 
                error_words_poz.append(word)      ### Append to error_words list if the given word appears less than 5 (as defined in the parameters of the embedding)
        return print('List of excluded words - Reason: Occuring less than 5!'+ "\n" + str(error_words_poz))

    

    def negative_list():    
        word_embedding_neg_loc = input('Give to location of the list of negative words to embed!')
        word_embedding_neg = input('Give the name of the negative list!')
        error_words_neg = []
        wb = Workbook()
        os.chdir(word_embedding_neg_loc)
        sheet2 = wb.add_sheet('Word_embedding_neg') 
        
        """
        Opening given negative list of words and using word2vec_mondat_model to embed each word, which yields the top 100 closest words
        """
        
        
        neg_list = open(word_embedding_neg+'.txt', encoding='utf-8')
        neg_list_2 = neg_list.read().split()
        rows = 0
        columns = 0
        for word in neg_list_2:
            columns = columns + 1
            try:
                embedding_i = word2vec_model_mondat.wv.most_similar(word, topn=100)
                sheet2.write(int(rows), int(columns), str(word+' '+'negative'))
                n = 0
                for v in embedding_i:
                    rows = rows + 1
                    n = n + 1
                    sheet2.write(int(rows),int(columns), str(v))
                    if n == 100:
                        rows = 0
                        wb.save('embedding_neg.xls') 


            except: 
                error_words_neg.append(word)      ### Append to error_words list if the given word appears less than 5 (as defined in the parameters of the embedding)
        return print('List of excluded words - Reason: Occuring less than 5!'+ "\n" + str(error_words_neg))
    
    def main():
        posizive_list()
        negative_list()
        
        
    if __name__ == "__main__":
        main()

        
if question == 'Two':
    
    
    """
    If the user only wants to embed a certain number of words, each printed on a seperate.txt
    """
        
    def input_szo():
        i = input('Input words one by one. If finished, input END!')
        while i != 'END!':
            try:
                model = word2vec_model_mondat.wv.most_similar(i, topn=100)
                with open(str(i+'.txt'), 'w') as file:
                    file.write(str(model)  + '\n')
                    i = input('Input word to embed!')
            except:
                print('Not in vocabulary!')
                i = input('Input word to embed!')
                
    def main_2():
        input_szo()

        
    if __name__ == "__main__":
        main_2()
        
        
        

