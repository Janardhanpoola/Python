import os
import pandas
import time

while True:
    if os.path.exists("weather.csv"):
        data=pandas.read_csv("weather.csv")
        print(data.mean()["st1"])
        break
    else:
        print("filenotfound")
   


#############3

import numpy as np

df=np.arange(9).reshape(3,3)

print(df>=0)

##################

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

arr[arr%2==1]=-1

print(arr)
##########

arr = np.arange(10)
out = np.where(arr % 2 == 1, -1, arr)
print(arr)
print(out)

##############

arr=np.arange(10).reshape(2,-1)

print(arr)

################

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

res=np.hstack([a,b])
print(res)

################


a = np.array([1,2,3])

res=np.r_[np.repeat(a,3),np.tile(a,3)]

print(res)

##########
