def main():
	encrypted = input()
	key = input()
	letters = {"A":0, "B":1, "C":2 ,"D":3, "E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"O":14,"P":15,"Q":16,"R":17,"S":18,"T":19,"U":20,"V":21,"W":22,"X":23,"Y":24,"Z":25}
	numLetters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	
	tot = len(encrypted)
	keyTot = len(key)
	retStr = ""
	
	done = 0  
	while len(retStr) < tot:
		leftIndex = 0 if done==0 else done - keyTot 
		rightIndex = leftIndex + keyTot
		for i in range(leftIndex, rightIndex):
			if(done >= tot):
				break
			eL = encrypted[done]
			nL = 0
			if(len(retStr) < keyTot):
				nL = key[i]
			else:
				nL = retStr[i]
			shift = letters[eL] - letters[nL]
			shift = shift if shift >= 0 else shift + 26
			retStr += numLetters[shift]
			done += 1
	print(retStr)
main()