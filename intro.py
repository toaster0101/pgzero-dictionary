dictionary={"England":"London","France":"Paris"}
print(dictionary)
dictionary["America"]="New York"
print(dictionary)
if "America" in dictionary:
    print("yay")
else:
    print("nay")
x=input("what country")
print(dictionary[x])