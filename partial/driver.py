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
        # time until current gate opens
        openingTime = openTimes[i] - i - loopTime
        # at least one hour will be spent on current gate
        timeSpentOnGate.append(1)
        if(openingTime <= 0):  # current gate is open
            if(i == (gates - 1)):  # if it is the last one, we're done!
                break
            if(prices[i] < cheapestPrice):  # check if current gate's price is the cheapest
                cheapestPrice = prices[i]
                cheapestRoad = i  # finding cheapeast gate to loop through to minimize cost
        else:
            openingTime = openingTime if (
                openingTime % 2 == 0) else openingTime + 1  # number of hours spent must be odd(1 is already added so this calculation should return lowest even number) since we're going back and forth. full loop must always be even
            timeSpentOnGate[cheapestRoad] += openingTime
            loopTime += openingTime  # i + loopTime is the total time spent so far
    retInt = 0
    for j in range(len(prices)):
        # calculates and returns total cost of traveling
        retInt += prices[j] * timeSpentOnGate[j]
    print(retInt)
    return


main()
