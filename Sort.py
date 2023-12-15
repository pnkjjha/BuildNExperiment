# Pankaj Jha
#12/11/23
#  repeat i= 1 to n
#  repeat j= i+1 to n
#  compare Ni, N(i+j) == true
#  swap Ni,N(i+j)
# An array is sorted when there is every number is less than all subsequent number

def swap(firstItem, secondItem):
    """ Swap the value of firstItem and second Item and returns
    """
    tempVar = firstItem
    firstItem = secondItem
    secondItem = tempVar
# dont know if this is possible
    return firstItem, secondItem

sortList = [2, 3, 9, 4, 7, 8, 1]

  
for i in range(len(sortList)-1):
    for j in range(i+1,len(sortList)): 
        if sortList[i] >= sortList[j]: 
            sortList[i], sortList[j] = swap(sortList[i], sortList[j]) 

print(sortList)
