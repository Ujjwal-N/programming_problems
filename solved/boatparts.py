def main():
	parts = set()
	firstLine = input().split()
	partsInt = int(firstLine[0])
	days = int(firstLine[1])
	for i in range(days):
		currInput = str(input())
		if(not(currInput in parts)):
			parts.add(currInput)
		if(len(parts) >= partsInt):
			print(i + 1)
			return
	print("paradox avoided")


main()