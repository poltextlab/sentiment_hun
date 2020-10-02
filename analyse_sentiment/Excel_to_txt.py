#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
from user_options import answer


# In[ ]:


import pandas as pd
import os


# In[ ]:


def import_excel():
    name = answer.excel_name
    excel = pd.read_excel(name+'.xlsx', encoding='utf-8')
    index = answer.excel_column
    content = answer.excel_content
    os.chdir(answer.base_dir)
    os.chdir('.\output')
    for n,m in zip(excel[str(index)], excel[str(content)]):
        with open(str(n+'.txt'), 'w', encoding='utf-8') as file:
            file.write(m)


# In[ ]:


import_excel()

