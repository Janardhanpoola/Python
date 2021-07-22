#my_file=open("fruits.txt")
#print(my_file.read())

############
#file cursor

my_file=open("fruits.txt")
content=my_file.read()
print(content)
print(content)

#########

#writing a text to a file

with open("fiile1/veggies.txt","w") as my_file:
    my_file.write("tomato\tcarrot\tcucumber")

##########
#count no of occurence

############



def foo(character, filepath="fiile1/bear.txt"):
    file = open(filepath)
    content = file.read()
    return content.count(character)
    
print(foo(" is "))

###############
#writing chars of one file to other

with open("fiile1/bear.txt") as myfile:
    content=myfile.read()
    extract_content=content[:90]

with open("fiile1/veggies.txt","w") as file2:
    file2.write(extract_content)

#################
#adding the contents to the existing file
#lets add hey im hero in bear.txt


with open("fiile1/bear.txt","a+") as myfile:  #to read and append use a+
    myfile.write("hey im ")#the cursor will be to the EOL
    myfile.seek(0)#setting the cursor to the top line
    content=myfile.read()
print(content)

############################
#copy contents of bear1 to bear2

with open("fiile1/bear1.txt") as myfile:
    content=myfile.read()
with open("fiile1/bear2.txt","w") as myfile:
    myfile.write(content)

###########################3
#append the contents of bear1 to bear2

with open("fiile1/bear1.txt") as myfile:
    content=myfile.read()
with open("fiile1/bear2.txt","a") as myfile:
    myfile.write(content)
####################

with open("fiile1/smpl.txt") as myfile:
    print("]]]]]]]]]]")
    content=myfile.read()
   # print(content)
    for line in myfile:
        line=line.rstrip()
        if line:
            print(line)

###################

def readn(path,n):
    with open(path,"r") as f:
        content=f.readlines()
        print(content)
        print(content[n])
    

path="fiile1/bear.txt"
n=4
readn(path,n)