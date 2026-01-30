input=input("Enter something : ")
vowelList={"a":0,"e":0,"i":0,"o":0,"u":0}
for i in input:
    if i in vowelList:
        vowelList[i]+=1
print(vowelList)