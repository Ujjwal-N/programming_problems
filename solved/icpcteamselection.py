import random
import math
nums = []


def main():
    global nums
    numDataSets = int(input())
    for i in range(numDataSets):
        currLen = int(input()) * 3
        numStrings = input().split()
        for item in numStrings:
            binSearchAppend(int(item))
        i = int(currLen / 3)
        retInt = 0
        while(i < currLen):
            retInt += nums[i]
            i += 2
        print(retInt)
        nums = []


def binSearchAppend(val):
    global nums
    recuseSearch(0, (len(nums)-1), val)


def recuseSearch(low, high, val):
    global nums
    currLen = len(nums)
    if(currLen < 1):
        nums.append(val)
        return

    if (abs(high - low) > 1):
        mid = (high + low) // 2
        if nums[mid] == val:
            nums.insert(mid, val)
        elif(nums[mid] > val):
            recuseSearch(low, mid - 1, val)
        else:
            recuseSearch(mid + 1, high, val)
    else:
        if(val < nums[low]):
            nums.insert(low, val)
        elif(val > nums[high]):
            if(high == (currLen - 1)):
                nums.append(val)
            else:
                nums.insert(high + 1, val)
        else:
            nums.insert(high, val)


def testSortingAlgo():
    for i in range(1):
        numStrings = []
        for i in range(10):
            randStr = str(random.randint(0, 5))
            numStrings.append(randStr)
        # nums = []
        for item in numStrings:
            binSearchAppend(int(item))

        print(nums)


main()
