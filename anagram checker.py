scramble=input("scrambled ver. here: ")
clear=input("unscrambled ver. here: ")
scrambleL=list(scramble.lower())
clearL=list(clear.lower())
clearL.sort()
scrambleL.sort()
print(clearL)
print(scrambleL)
if clearL==scrambleL:
    print("yay")
else:
    print("nay")