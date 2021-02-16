# passes only first 3
# reminder that toll is not collected at gates, but instead at roads
# easiest way to visualize this is have the toll be collected at the halfway point of the road connecting two gates
# came full circle in my debugging efforts so I gave up. Maybe the problem is broken?
def main():
    gates = int(input())
    prices = [int(i) for i in input().split(" ")]
    openTimes = [int(i) for i in input().split(" ")]
    cheapestRoad = 0
    cheapestPrice = prices[0]
    timeSpentOnGate = []
    loopTime = 0
    for i in range(gates):
        openingTime = openTimes[i] - i - loopTime
        timeSpentOnGate.append(1)
        if(openingTime <= 0):  # no need to loop
            if(i == (gates - 1)):
                break
            if(prices[i] < cheapestPrice):
                cheapestPrice = prices[i]
                cheapestRoad = i
        else:
            openingTime = openingTime if (
                openingTime % 2 == 0) else openingTime + 1
            timeSpentOnGate[cheapestRoad] += openingTime
            loopTime += openingTime
    retInt = 0
    for j in range(len(prices)):
        retInt += prices[j] * timeSpentOnGate[j]
    print(retInt)
    return


main()
