#!/usr/bin/env python
# coding: utf-8

# In[12]:


import os
class answer:
    def __init__(self):
        self.base_dir = str(os.getcwd())
        self.excel_loc = '.\INPUT_FILE'
        self.excel_name = input('Input the excel name!')
        self.excel_column = input('Input the name of the column containing ids of the articles!')
        self.excel_content = input('Input the content column!')
        self.dict_loc = input('Input the location of the dictionaries')
        self.dict_name_pos = input('Input the positive dictionary!')
        self.dict_name_neg = input('Input the negative dictionary!')
          
def answer_return():
    return answer()
    

answer = answer_return()

