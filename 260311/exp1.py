import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

s=pd.Series([1,3,5,np.nan,6,8]) #值的类型会自动统一
s.sort_values()
s.values
s.index
s2 = pd.Series([3,51,5,2,6],index=['a','b','c','d','e'])#自己定义索引

dates=pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.random.randn(6,5),index=dates,columns=list('ABCDE'))

df2=pd.DataFrame({'A':1.,
 'B':pd.Timestamp('20130102'),
 'C':pd.Series(1,index=list(range(4)),dtype='float32'),
 'D':np.array([3]*4,dtype='int32'),
 'E':pd.Categorical(['test','train','test','train']),
 'F':'foo'})

data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
 'year':[2000, 2001, 2002, 2001, 2002],
 'pop':[1.5, 1.7, 3.6, 2.4, 2.9]}
df3 = pd.DataFrame(data,columns=['year', 'state', 'pop', 'debt'],
 index=['one', 'two', 'three', 'four', 'five'])
df3['debt']=16 #给一个列（column）赋值

print(df.loc['20130102':'20130104',['A']])
#print(df.loc[:,['A','B']])
#print(df.sort_values(by='A'))
#print(df.loc[dates[0]])
#print(df.T)
# print(df)
# print(df.describe())
# print(df.head(10))
# print(df.tail(3))
# print(df.index)
# print(df.columns)
# print(df.values)
#print(df3)
#print(df2.dtypes)
#print(df)
#print('c' in s2.index)
#print(s2[['a','d','c']])
#print(s.index)
#print(s.values)
#print(s.sort_values())