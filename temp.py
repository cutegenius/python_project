# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
path='C:\\Users\\37212\\Desktop\\'


lst1= pd.read_excel(path+'基金经理大全.xlsx',index_col=0,header=[0,1])
lst2= pd.read_excel(path+'基金经理对比.xlsx',index_col=0,header=[0,1])
lst1=lst1.dropna(how='all')
lst2=lst2.dropna(how='all')
lst1=lst1.reset_index()
lst2=lst2.reset_index()

#lst1.set_index(['基金经理','基金公司'],inplace=True)
#lst2.set_index(['基金经理','基金公司'],inplace=True)

lst3 = pd.merge(lst1,lst2,on=['基金经理','基金公司'])

lst3.to_excel("基金经理10年以上.xlsx")


lst3=lst1.append(lst2)

set1=cash['代码']
set2=all_stocks_code.iloc[:,0]

set1=tttt.index.tolist()
set2=pd.read_excel('C:\\Users\\37212\\Desktop\\oooo.xlsx')['行标签'].tolist()



samestocks=pd.Series(list(set(set1).intersection(set(set2))))


set1diff=list(set(set1).difference(set(samestocks)))
set2diff=list(set(set2).difference(set(samestocks)))##what I want


