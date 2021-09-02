def selSort(numList):
    lowIndex = 0
    for x in range(len(numList)-1):
        lowIndex = x
        for y in range(x+1,len(numList)):
            if (numList[y] < numList[lowIndex]):
                lowIndex = y
        if(lowIndex != x):
            numList[x], numList[lowIndex] = numList[lowIndex], numList[x]
    return numList;

nums = [5,8,4,4,3,52,34,53,22]
nums = selSort(nums)
print(nums)