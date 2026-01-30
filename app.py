currentD={}
print("\---Dictionary App---/")
while True:
    option=input("1-View Dictionary\n2-Add Entry And Definition\n3-Edit Entry And/Or Definition\n4-Remove " \
    "Entry And Defintion\n5-Close App\nChoose An Option:")
    if option=="1":
        print(currentD)
        continue
    elif option=="2":
        while True:
            newEntry=input("Please enter the name of the entry:")
            newEntryD=input("Please enter the definintion of the new entry:")
            if newEntry in currentD:
                print("There is already an entry with that name, please choose a new name")
                continue
            else:
                currentD[newEntry]=newEntryD
                break
    elif option=="3":
        entryEditChoice=input("Please select the entry you would like to edit:")
        if entryEditChoice not in currentD:
            print("There is no entry with that name, please select and existing entry")
            continue
        editN=input("Do you want to edit the name? (y/n)")
        if editN=="y":
            entryEdit=input("Please enter the new name of the entry:")
            entrydesc=currentD[entryEditChoice]
            currentD[entryEdit]=entrydesc
            del currentD[entryEditChoice]
        editD=input("Do you want to edit the description? (y/n)")
        if editD=="y":
            entryEditD=input("Please enter the new description of the entry:")
            if editN=="y":
                currentD[entryEdit]=entryEditD
            else:
                currentD[entryEditChoice]=entryEditD
    elif option=="4":
        entryDel=input("Please select which entry to delete:")
        if entryDel not in currentD:
            print("There is not an entry with that name, please select a existing entry")
            continue
    elif option=="5":
        break
    else:
        print("That is not an option")
        continue