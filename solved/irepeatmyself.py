def main():
    numInputs = int(input())
    for _ in range(numInputs):
        currStr = input()
        currLen = len(currStr)
        subLen = 1
        done = False
        while(not done):
            currFrag = currStr[:subLen]
            j = subLen
            while(True):
                endIndex = j + subLen
                endIndex = min(endIndex, currLen)
                secondFrag = currStr[j:endIndex]
                if(not truncatedCompare(currFrag, secondFrag)):
                    break
                if(endIndex == currLen):
                    done = True
                    break
                j += subLen
            if(not done):
                subLen += 1
        print(subLen)


def truncatedCompare(stringOne, stringTwo):
    iterLen = min(len(stringOne), len(stringTwo))
    for i in range(iterLen):
        if(stringOne[i] != stringTwo[i]):
            return False
    return True


main()
