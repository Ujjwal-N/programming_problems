import math
nCuts = -1
pows = 0
def main():
	global nCuts
	global pows
	nSquares = int(input())
	print(5//2)
	if(nSquares == 2 or nSquares == 1):
		print(str(nSquares) + " " + "0")
		return
	convertToBinary(nSquares)
	if(nCuts == 1):
		retStr = str(nSquares) + " 0"
		print(retStr)
		return

	power = int(math.pow(2,pows))
	retStr = str(power) + " " + str(nCuts)
	print(retStr)


def convertToBinary(num):
	global nCuts
	global pows

	if num > 1:
		convertToBinary(num // 2)
	pows += 1
	if(num % 2 == 1):
		nCuts = pows



main()