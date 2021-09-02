def bubbleSort(numList):
    iter = len(numList)
    while (iter > 0):
        for x in range(iter-1):
            if numList[x] > numList[x+1]:
                numList[x], numList[x+1] = numList[x+1],numList[x]
        iter -= 1
    return numList

nums = [6,9,34,17,4,5,6]
nums = bubbleSort(nums)
print(nums)
