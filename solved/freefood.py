def main():
    numDays = int(input())
    retInt = 0
    ranges = []
    for i in range(numDays):
        line = input().split(" ")
        startDay = int(line[0])
        endDay = int(line[1])
        toBeAdded = [startDay, endDay]
        ranges.append(toBeAdded)
    ranges = sorted(ranges, key=lambda l: l[0], reverse=False)
    lStart = 366
    lEnd = -1
    for rangeL in ranges:
        if(lEnd < rangeL[0]):
            retInt += rangeL[1] - rangeL[0] + 1
        else:
            if(rangeL[1] < lEnd):
                continue
            retInt += rangeL[1] - lEnd
        lStart = rangeL[0]
        lEnd = rangeL[1]
    print(retInt)


main()
