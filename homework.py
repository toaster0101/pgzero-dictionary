list={"404":"404 Means (BLANK) not found","500":"500 Means internal server error","409":"409 Means conflict","400":"400 Means bad request","403":"403 Means forbidden"}
print("List of HTML error codes (only 5 of them)\n|1.404\n|2.500\n|3.409\n|4.400\n|5.403")
while True:
    Choice=input("Select which one you would like to view the meaning of (1-5):")
    if Choice=="404":
        print(list["404"])
    elif Choice=="500":
        print(list["500"])
    elif Choice=="409":
        print(list["409"])
    elif Choice=="400":
        print(list["400"])
    elif Choice=="403":
        print(list["403"])
    else:
        print("-----404-----\nCode not found")