# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
path='C:\\Users\\37212\\Desktop\\'


lst1= pd.read_excel(path+'基金经理1.xlsx')
lst2= pd.read_excel(path+'基金经理2.xlsx')


set1=cash['代码']
set2=all_stocks_code.iloc[:,0]
set1=tttt.index.tolist()
set2=pd.read_excel('C:\\Users\\37212\\Desktop\\oooo.xlsx')['行标签'].tolist()



samestocks=pd.Series(list(set(set1).intersection(set(set2))))


set1diff=list(set(set1).difference(set(samestocks)))
set2diff=list(set(set2).difference(set(samestocks)))##what I want

