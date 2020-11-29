def main():
	num = int(input())
	sums = 1 + num
	for i in range(2,num + 1):
		for ix in range(i, num + 1):
			# if(euclidean(i,ix) == 1):
			# 	sums += 1
			pass
	print(sums)

def euclidean(quotient, remainder):
	if(remainder <= 0):
		return quotient	
	nRemainder = quotient % remainder
	return euclidean(remainder, nRemainder)


main()