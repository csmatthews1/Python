def insertSort (numList):
    for x in range(len(numList)-1):
        if(numList[x+1] < numList[x]):
            movVal = numList[x+1]
            for y in range(x+1,0,-1):
                if(numList[y-1] > movVal):
                    numList[y] = numList[y-1]
                    insertIndex = y-1
            numList[insertIndex] = movVal
    return numList

nums = [5,8,4,4,3,52,34,53,22]
nums = insertSort(nums)
print(nums)

