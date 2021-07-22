with open("fiile1/conf.txt","r") as myfile:
    count=0
    content=myfile.readlines()
    for line in content:
        if "CONFIG" in line:
            count+=1
    print(count)