lens = input().split()
firstSet = list(input())
secondSet = list(input())
time = int(input())

lenOne = int(lens[0])
lenTwo = int(lens[1])

strOne = []
ants = {}


for i in range(len(firstSet)):
	strOne += firstSet[len(firstSet) - i - 1]
	ants[firstSet[i]] = 0

for i in secondSet:
	strOne += i
	ants[i] = 1

lenStr = len(strOne) - 1

#print(ants)
for i in range(time):
	swappedAnts = []
	for ix in range(lenStr):
		if(strOne[ix] == "C"):
			#print(strOne)
			pass
		if not(strOne[ix] in swappedAnts) and not(strOne[ix+1] in swappedAnts):
			#print("passed first if")
			if(ants[strOne[ix]] == 0 and ants[strOne[ix+1]] == 1):
				#print("passed second if")
				if(not(ix == 0 and ants[strOne[ix]] == 1) and not(ix == lenStr and ants[strOne[ix+1]] == 0)):
					#print("passed third if")
					if(ants[strOne[ix]] == 0 and ants[strOne[ix+1]] == 1):
						temp = strOne[ix]
						swappedAnts.append(temp)
						strOne[ix] = strOne[ix+1]
						swappedAnts.append(strOne[ix])
						strOne[ix+1] = temp
				else:
					

					pass
					#print("avoided last flip")

	#print(strOne)
retStr = ""
for i in strOne:
	retStr += i

print(retStr)
