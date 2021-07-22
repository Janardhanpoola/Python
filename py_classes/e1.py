class Robot:
    def __init__(self,name,color,weight):
        self.name=name
        self.color=color
        self.weight=weight
    
    def Introduceself(self):
        return f'Hello world,Im {self.name}'


r1=Robot("Tom","red",40)
r2=Robot("jerry","blue",30)

print(r1.Introduceself())

############

class Person:
    def __init__(self,name,personality,isSitting,RobotOwned):
        self.name=name 
        self.personality=personality
        self.isSitting=isSitting
        self.RobotOwned=RobotOwned

    def sit_down(self):
        self.isSitting=True
    
    def stand_up(self):
        self.isSitting=False



p1=Person('punith','Aggressive',False,r2)

p2=Person('me','calm',True,r1)

p1.sit_down()

p2.stand_up()

print(p1.isSitting)

print(p2.isSitting)

p1_robot=p1.RobotOwned.name

print(p1_robot)



################


records=[
    ('foo',1,2),('bar','hello'),('foo',3,4),
]

def do_foo(x,y):
    print('foo',x,y)

def do_bar(x):
    print('bar',x)

for tag,*args in records:
    if tag=='foo':
        do_foo(*args)
    elif tag=='bar':
        do_bar(*args)
###################


line='nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
line=line.split(":")
a,*b,home_dir,path=line

print(home_dir,path)
#########

record=('ACME',50,123.45,(12,18,2012))

name,a,_,(*u,y)=record

print(name,y)

###########

d1={'empid':[189,290,31,41,5],'empname':['a','b','c','d','e']}

vals=list(d1.values())

d={}
for i in zip(vals[0],vals[1]):
    d[i[0]]=i[1]
    
#d=sorted(d.items(),key=lambda x:x[0])
print(d)
print(dict(sorted(d.items())))




# import requests
# import json

# def clean_data():
#   r = requests.get('https://coderbyte.com/api/challenges/json/json-cleaning')
#   return r.json()

# #print(clean_data())

# res=clean_data()

# keys=res.keys()

# vals=list(res.values())

# print(vals)
# filters=['N/A','-','']
# for i in vals:
#   d={}
#   if type(i)==dict:
#     for k,v in i.items():
#       pass

#   elif type(i)==list:
#     for each in i:
#       for item in filters:
#         if item==each:
#           i.remove(item)

#   else:
#     for item in filters:
#       if item==i:
#         vals.remove(item)

# print(vals)

sm_dict={'name': {'first': 'Robert', 'middle': '', 'last': 'Smith'}, 
'age': 25, 'DOB': '-', 'hobbies': ['running', 'coding', '-'],
 'education': {'highschool': 'N/A', 'college': 'Yale'}}


filters=['N/A','-',""]

res={k:v for k,v in sm_dict.items() if v not in filters}

print(res)

d={}
for k,v in res.items():
    if type(v)==dict:
        print(v)
        va={k:v for k,v in v.items() if v not in filters}
        d[k]=va
    elif type(v)==list:
        for i in v:
            if i in filters:
                v.remove(i)
        d[k]=v
    else:
        d[k]=v
print(d)





##########

sum=6
total=5
ls=[1,2,3,4,5]
res=[]

for i in range(0,len(ls)):
    for j in range(1,len(ls)):
        if ls[i]+ls[j]==sum:
            res.append((ls[i],ls[j]))
print(res)

a,b=res[0]
print(a,b)
########

s1='pqruvs'
s2='pqrxy'

diff=(list(set(s1)-set(s2))+list(set(s2)-set(s1)))

res="".join(diff)

print(res)
############


import copy

li1=[1,2,3,4,5]

print(li1)

li2=copy.deepcopy(li1)

li2[0]=25

print(li2)
print(li1)
################

text = "This is a test from a test ok" 

firstTest = text.find('test')

print(firstTest)

print(text.find('test', firstTest + 1))

################

def sample():
    yield 1
    yield 2

x=sample()
print(x.__next__())

###############

def smpl(**rgs):
    return rgs

print(smpl(a=1,b=2))