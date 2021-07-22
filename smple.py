e=[]
with open("fiile1/smpl.txt","r") as myfile:
    content=myfile.readlines()
    print(content)
    for x in content:
        val=x.rstrip()
        e.append(val)
    print(e)

with open("fiile1/smpl2.txt","w") as myfile:
    myfile.write("\n".join(e))



    