def main():
    lineOne = input().split(" ")
    numItems = int(lineOne[1]) + 2
    partitions = [int(x) for x in input().split(" ")]
    partitions.append(int(lineOne[0]))
    partitions.insert(0, 0)

    possLengths = set()
    for i in range(numItems):
        for k in range(i + 1, numItems):
            possLength = partitions[k] - partitions[i]
            possLengths.add(possLength)

    possLengths = sorted(possLengths)
    printStr = ""
    for j in possLengths:
        printStr += str(j) + " "
    print(printStr[:-1])


main()
