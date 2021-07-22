import pandas as pd  
df1=pd.DataFrame([[1,2,3],[4,5,6]])
print(df1)

###############
# Mentioning column name 
#######################

df2=pd.DataFrame( [[10,20,30],[40,50,60]],columns=["Price","Age","value"])
print(df2)

###############
#Mentioning row name
###############

df3=pd.DataFrame( [[10,20,30],[40,50,60]],columns=["Price","Age","value"],index=["first","second"])
print(df3)

###############
#Dataframe as Dictionary
##############

df4=pd.DataFrame([{"name":"A","rollno":56,"gender":"M"},{"name":"B","rollno":57,"gender":"F"}   ])
print(df4)