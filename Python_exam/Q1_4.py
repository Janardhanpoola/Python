#1. Given a string, return a new string where "not " has been added to the front. However, if the
#string already begins with "not", return the string unchanged.


def not_string(str):

    if str.startswith('not'):
        return str
    else:
        return "not "+str

if __name__=="__main__":
    str="candy"
    print(not_string(str))


##############################

#2.Implement an appropriate Unit Test for the not_string method.

import unittest

class Test_not_string(unittest.TestCase): #python -m unittest test.py
    def test_not_string(self):
        self.assertEqual(not_string("candy"),"not candy") #pass case
        self.assertNotEqual(not_string("not candy"),"candy") #pass case
        #self.assertEqual(not_string('candy'),'candy') #fail case

#########################################


#3.Implement the unique_names method. When passed two lists of names, it will return a list
#containing the names that appear in either or both lists. The returned list should have no
#duplicates.

def uniq_names(ls1,ls2):
    l3=ls1+ls2
    return list(set(l3))


ls1=['Ava', 'Emma', 'Olivia']
ls2=['Olivia', 'Sophia', 'Emma']

print(uniq_names(ls1,ls2))


###############################

#4.In python code, given a JSON object with nested objects, write a function that flattens all the
#objects to a single key-value dictionary. Do not use the lib that actually performs this function.
import json


def make_it_flat(d):
    k="".join(list(d.keys()))
    dv=list(d.values())[0]

    vals=list(dv.values())

    keys=[k+'_'+i for i in list(dv.keys())]

    

    res=dict((zip(keys,vals)))
    return res

d={
"a": {
"b": "c",
"d": "e"
}
}
print(make_it_flat(d))

##########

import sqlite3

conn=sqlite3.connect('chinook.db')
c=conn.cursor()
c.execute('select * from tracks')
data=c.fetchall()

for i in data:
    print(i)
