import random
import math
nums = []
def main():
	global nums
	input()
	input()
	numStrings = input().split()
	tLen = len(numStrings) - 1
	for item in numStrings:
		binSearchAppend(int(item))
	i = 1
	retSum = 0
	while(i < tLen):
		retSum += nums[i]
		i += 3
	#print(nums)
	print(retSum)

def binSearchAppend(val):
	global nums
	recuseSearch(0, (len(nums)-1),val)
def recuseSearch(low, high,val):
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
		#nums = []
		for item in numStrings:
			binSearchAppend(int(item))

		print(nums)
testSortingAlgo()