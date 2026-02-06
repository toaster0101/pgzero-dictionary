lettersS={}
for i in range(97,123,1):
    lettersS[chr(i)]=0
lettersC={}
for i in range(97,123,1):
    lettersC[chr(i)]=0
scramble=input("scrambled ver. here: ")
clear=input("unscrambled ver. here: ")
for i in scramble:
    lettersS[i]+=1
for i in clear:
    lettersC[i]+=1
if lettersC==lettersS:
    print("yar")
else:
    print("nar")