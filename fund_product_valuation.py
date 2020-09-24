# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:08:33 2020

@author: 37212
"""
import numpy as np
import pandas as pd
import os
'''
变量输入区
company_name：基金公司全称
product_name：产品名称
'''
company_name='广发基金管理有限公司'
product_name='广发中证500指数增强型证券投资基金'
'''
原始数据导入区
基金公司规模.xlsx：下载路径wind——基金公司——基金公司规模（截止日期选择最新日期即可，导出excel到桌面）
基金公司经理变更.xlsx：下载路径wind——基金公司——基金公司经理变更（截止日期选择最新日期即可，导出excel到桌面）
'''
path='C:\\Users\\37212\\Desktop\\'
companysize=pd.read_excel(path+'基金公司规模.xlsx',index_col=0,header=[0,1])
companysize=companysize.dropna(how='all')
fundmanagerchange=pd.read_excel(path+'基金公司经理变更.xlsx',index_col=0,header=[0,1])
fundmanagerchange=fundmanagerchange.dropna(how='all')
fundmanagerchange=fundmanagerchange.rank(pct=True)
'''
打分计算区
first_1：基金公司评价-基金经理数量
first_2：基金公司评价-公司管理基金规模
first_3：基金公司评价-公司产品线布局情况
second_1：产品设计-投资主题
second_2：产品设计-投向
third_1：销售时机-同类型产品规模变动情况（季度）
third_2：销售时机-同类型产品规模变动情况（年度）
third_3：销售时机-同类型产品新发行增量情况（月度）
third_4：销售时机-同类型产品新发行增量情况（季度）
'''
target_company_manager=fundmanagerchange.ix[company_name]
first_1=target_company_manager.loc['Unnamed: 1_level_0']['基金经理数']*10
target_company_size=companysize.ix[company_name]
first_2=min(target_company_size.loc['基金资产净值合计(亿元)']['全部']/50,10)
first_3_1=2 if target_company_size.loc['基金资产净值合计(亿元)']['货币市场型']>0 else 0
first_3_2=2 if target_company_size.loc['基金资产净值合计(亿元)']['股票型']>0 else 0
first_3_3=2 if target_company_size.loc['基金资产净值合计(亿元)']['混合型']>0 else 0
first_3_4=2 if target_company_size.loc['基金资产净值合计(亿元)']['债券型']>0 else 0
first_3_5=2 if (target_company_size.loc['基金资产净值合计(亿元)']['另类投资']>0)or(target_company_size.loc['基金资产净值合计(亿元)']['QDII']>0) else 0
first_3=first_3_1+first_3_2+first_3_3+first_3_4+first_3_5
second_1=5
second_2=5





