passwordL={"dave":"daveTheBest","oogler124":"123456"}
login=input("username=")
if login not in passwordL:
    print("incorrect username")
else:
    loginP=input("password=")
    if loginP != passwordL[login] :
        print("incorrect password")
    else:
        print("yay")