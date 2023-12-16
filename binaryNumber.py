#Pankaj jha
#16/12/23

decimalValue = 37
remainderList = []

while decimalValue >=1 :
    remainderList.append(decimalValue%2)
    decimalValue=decimalValue/2 

print("Binary number is\n")
for d in reversed(remainderList):
    print(int(d), end="")

