input=input("enter numbers :")
numList="0123456789"
blacklist=[]
numCount=0
for i in input:
    if i in numList:
        if i not in blacklist:
            numCount+=1
            blacklist.append(i)
if numCount==10:
    print("yes")
else:
    print("no")