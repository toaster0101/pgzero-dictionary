input=input("enter numbers :")
numList={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
for i in input:
    if i in numList:
        numList[i]+=1
x=0
for j in numList.values():
    if j==0:
        x=1
if x!=1:
    print("yes")
else:
    print("no")