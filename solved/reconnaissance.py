def main():
	#reading inputs
	numInputs = int(input())
	firstInput = input().split()

	inputs = [ [ 0 for y in range( 2 ) ] for x in range( numInputs ) ]

	inputs[0][0] = int(firstInput[0])
	inputs[0][1] = int(firstInput[1])


	for i in range(1,numInputs):
		currInput = input().split()
		inputs[i][0] = int(currInput[0])
		inputs[i][1] = int(currInput[1])
		
	#finding the lowest and highest possible times
	lowestTime = 0
	highestTime = 1000000
	
	#doing this calc here for an edge case where the while loop does not execute at all
	lowComp = (2*lowestTime + highestTime) / 3
	lowRange = findRange(lowComp,inputs) 
	
	while((highestTime - lowestTime) > 0.001):
		lowComp = (2*lowestTime + highestTime) / 3
		highComp = (lowestTime + 2 * highestTime) / 3
		lowRange = findRange(lowComp,inputs) #finds max distance between 2 lines
		highRange = findRange(highComp,inputs)

		if(lowRange < highRange):
			highestTime = highComp
		else:
			lowestTime = lowComp
	print(lowRange)



def findRange(time,inputs): 
	highPos = -float("inf")
	lowPos = float("inf")
	for inp in inputs: #finds all of the positions of all lines at each time
		cPos = inp[0] + time * inp[1]
		if(cPos > highPos):
			highPos = cPos
		if(cPos < lowPos):
			lowPos = cPos
	return abs(highPos - lowPos)

main()