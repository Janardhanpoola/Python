def foo(*args):
    lst=[]
    for i in args:
        lst.append(i.upper())
    return sorted(lst)
print(foo("snow","zeer","helli"))

###############

import pandas as pd 

import numpy as np


df=pd.DataFrame(np.random.rand(4,4),['A','B','C','D'],['X','Y','Z','Q'])  # rand prints randoms b/w 0 and 1

df1=pd.DataFrame(np.random.randn(4,4),['A','B','C','D'],['X','Y','Z','Q'])  # randn prints randoms from std. normal dist. 

test=df.iloc[1]

print(test)
print(df)
print(df1)