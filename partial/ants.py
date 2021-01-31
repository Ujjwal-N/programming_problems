def main():
    numCases = int(input())
    for i in range(numCases):
        case = [int(x) for x in input().split(" ")]
        ants = 0
        hLen = case[0] / 2
        maxDist = -1
        maxVal = -1
        minDist = hLen
        minVal = -1
        while(ants < case[1]):
            readAnts = [int(x) for x in input().split(" ")]
            for ant in readAnts:
                if(abs(ant - hLen) < minDist):
                    minDist = abs(ant - hLen)
                    minVal = ant

                if(abs(ant - hLen) > maxDist):
                    maxDist = abs(ant - hLen)
                    maxVal = ant
                ants += 1
        print("Min \n")
        print(minVal)
        print(minDist)

        print("Max \n")
        print(maxVal)
        print(maxDist)


main()
