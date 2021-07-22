from difflib import get_close_matches

possi=['apple','ape','asking']

word='appl'

#if len(get_close_matches(word,possi))>0:
print(get_close_matches(word,possi))
###########3


import numpy as np
import pandas as pd
import random
import cv2
img=cv2.imread('gid.jpg',0)

res=np.hstack((img,img))
print(res)

print("ok----------------")

res1=np.vstack((img,img))
print(res1)

r=np.random.rand()
print(r)
a=8
b=9

print(a and b)


###################

dt={'name':['A','B','C'],
                  'age':[12,13,14],
                  'loc':['K','J','L']
}
i=[4,5,6]
df=pd.DataFrame(dt,index=i)

print(df)

##############3333333333

from pprint import pprint
sl=[  { 'name':'akash',
        'result': [{'sub':'MATHS','grade':'A'},{'sub':'ENG','grade':'B'},{'sub':'PHY','grade':'C'}]
},
{   'name':'aanand',
    'result':[{'sub':'MATHS','grade':'B'},{'sub':'ENG','grade':'B'},{'sub':'PHY','grade':'B'}]
}

]

rows=[]

for data in sl:
    name=data['name']
    results=data['result']
    print(results)
    for result in results:
        result['name']=name
        rows.append(result)
print(rows)
df=pd.DataFrame(rows)


colum_titles=['name','sub','grade']

df=df.reindex(columns=colum_titles)

print(df)

###################

df = pd.DataFrame({'City':['New York', 'Parague', 'New Delhi', 'Venice', 'new Orleans'], 
                    'Event':['Music', 'Poetry', 'Theatre', 'Comedy', 'Tech_Summit'], 
                    'Cost':[10000, 5000, 15000, 2000, 12000]})

index=[pd.Period('02-2020'),pd.Period('03-2020'),pd.Period('04-2020'),pd.Period('05-2020'),pd.Period('06-2020')]

df.index=index



df=df.replace(to_replace='[nN]ew ',value='New_',regex=True)

print(df)

#############################


df = pd.DataFrame({'City':['New York (City)', 'Parague', 'New Delhi (Delhi)', 'Venice', 'new Orleans'], 
                    'Event':['Music', 'Poetry', 'Theatre', 'Comedy', 'Tech_Summit'], 
                    'Cost':[10000, 5000, 15000, 2000, 12000]}) 

df=df.replace(to_replace='\(.*\)',value='',regex=True)

df=df.replace(to_replace='[nN]ew ',value='New_',regex=True)


print(df)

#################


df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'], 
                   'Product':[' UMbreLla', '  maTress', 'BaDmintoN ', 'Shuttle'], 
                   'Updated_Price':[1250, 1450, 1550, 400], 
                   'Discount':[10, 8, 15, 10]}) 
  
# Print the dataframe 
Product=[]
for i in df['Product']:
    Product.append(i.strip().capitalize())
df['Product']=Product

print(df)

import numpy as np
##########################
column = ['a', 'b', 'c', 'd', 'e'] 
index = ['A', 'B', 'C', 'D', 'E'] 
   
# create a dataframe of random values of array  
df1 = pd.DataFrame(np.random.rand(5, 5),  
        columns = column, index = index) 
print(df1)
# create the new index for rows 
new_index =['U', 'A', 'B', 'C', 'Z'] 
  
print(df1.reindex(new_index))

########################################

initial_data = {'First_name': ['Ram', 'Mohan', 'Tina', 'Jeetu', 'Meera'],  
        'Last_name': ['Kumar', 'Sharma', 'Ali', 'Gandhi', 'Kumari'],  
        'Age': [42, 52, 36, 21, 23],  
        'City': ['Mumbai', 'Noida', 'Pune', 'Delhi', 'Bihar']} 

df=pd.DataFrame(initial_data ) #,columns = ['First_name', 'Last_name','Age', 'City'])

print(df)


#############

df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/11'],  
                    'Event':['Music', 'Poetry', 'Theatre', 'Comedy'],  
                    'Cost':[10000, 5000, 15000, 2000]})  
  
# Create an empty list  
Row_list =[]  
    
# Iterate over each row  
for i in range((df.shape[0])):  
    
    # Using iloc to access the values of   
    # the current row denoted by "i"  
    print(list(df.iloc[i,:]))
    #Row_list.append(list(df.iloc[i, :]))  
    
# Print the first 3 elements  
print(Row_list[:3])  


########################

data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],  
        'Age':[27, 24, 22, 32],  
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],  
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}  
    
# Convert the dictionary into DataFrame   
df = pd.DataFrame(data)  

print(df)
    
# select three rows and two columns  
#print(df.loc[1:3, ['Name', 'Qualification']]) 
print("==============")
print(df.iloc[1:4,0:4:3])
print(df.loc[1:3,['Name','Qualification']])



##################


import pandas as pd 

import numpy as np


df=pd.DataFrame(np.random.rand(4,4),['A','B','C','D'],['X','Y','Z','Q'])  # rand prints randoms b/w 0 and 1

df1=pd.DataFrame(np.random.randn(4,4),['A','B','C','D'],['X','Y','Z','Q'])  # randn prints randoms from std. normal dist. 


print(df)
print(df1)