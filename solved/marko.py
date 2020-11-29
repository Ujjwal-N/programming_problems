import string

def split(word): 
    return [char for char in word] 

letters = list(string.ascii_lowercase)
def findChars(num):
    global letters
    startIndex = (num - 2) * 3
    endIndex = startIndex + 3
    if(num > 6):
        if(num == 7):
            endIndex = endIndex + 1
        elif(num == 8):
            startIndex = startIndex + 1
            endIndex = endIndex + 1
        elif(num == 9):
            startIndex = startIndex + 1
            endIndex = endIndex + 2
    return [letters[i] for i in range(startIndex, endIndex)]

def findNum(char):
	global numLetters
	for i in range(2, 10):
		if(char in findChars(i)):
			return i
	return -1

def main():
	d = {}
	nums = int(input())
	for i in range(nums):
		currLetters = split(input())
		addStr = ""
		for letter in currLetters:
			addStr += str(findNum(letter))
		if addStr in d:
			d[addStr] = d[addStr] + 1
		else:
			d[addStr] = 1
	dKey = input()
	if(dKey in d):
		print(d[dKey])
	else:
		print(0)

main()