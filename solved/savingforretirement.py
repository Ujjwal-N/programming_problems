import math


def main():
    readLine = input().split(" ")
    bR = int(readLine[1])
    b = int(readLine[0])
    bS = int(readLine[2])
    aS = int(readLine[4])
    A = int(readLine[3])
    numerator = bS * (bR - b)
    retAge = numerator / aS
    retAge = math.ceil(retAge) if numerator % aS != 0 else int(retAge + 1)
    print(retAge + A)


main()
