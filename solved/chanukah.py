def main():
    numCases = int(input()) + 1
    for i in range(1, numCases):
        currentCase = input().split(" ")
        nights = int(currentCase[1])
        candles = (nights * nights) + 3 * nights
        candles = candles // 2
        print(str(i) + " " + str(candles))


main()
