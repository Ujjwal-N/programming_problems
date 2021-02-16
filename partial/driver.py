# passes only first #3
# reminder that toll is not collected at gates, but instead at roads
# easiest way to visualize this is have the toll be collected at the halfway point of the road connecting two gates
# came full circle in my debugging efforts so I gave up
def main():
    gates = int(input())
    prices = [int(i) for i in input().split(" ")]
    openTimes = [int(i) for i in input().split(" ")]
    highTime = -1  # once the gate with the highest time is open, the enitre city will open
    highGate = -1
    for i in range(gates):
        if(openTimes[i] >= highTime):
            highTime = openTimes[i]
            highGate = i
    currRoad = 0
    nextAvailableGate = 1  # stores the next gate that cannot be opened yet
    cost = 0
    time = 0
    while(True):  # loop runs when the cost is optimized given the set of currently opened gates, so it runs again when the adjacent gate opens
        # check if possible to go straight through
        dis = highGate - currRoad  # accounting for travel time
        if(openTimes[highGate] <= (time + dis)):
            cost += calcCost(prices[currRoad:gates])
            print(cost)
            return
        else:
            if(currRoad == (gates - 1)):
                cost += calcCost(prices[currRoad:gates])
                print(cost)
                return

            # find cheapest gate to loop through
            cheapestPrice = prices[currRoad]
            cheapestRoad = currRoad

            # finding the first gate we cannot get through and the cheapest gate in all of the gates we can get through and accounting for travel time
            while((time + nextAvailableGate - currRoad) >= openTimes[nextAvailableGate]):
                nextAvailableGate += 1
                # nextAvailableGate - 1 gives the road before it, which is the furthest road that is accessible
                if(prices[nextAvailableGate - 1] <= cheapestPrice):
                    cheapestPrice = prices[nextAvailableGate - 1]
                    cheapestRoad = nextAvailableGate - 1

            timeToKill = openTimes[nextAvailableGate] - \
                (time + nextAvailableGate - currRoad)
            # traveling to the cheapest road and updating time with travel time
            time += cheapestRoad - currRoad
            timeToKill -= cheapestRoad - currRoad
            # updating the cost of traveling to the cheapest road
            cost += calcCost(prices[currRoad: cheapestRoad])
            currRoad = cheapestRoad  # updating position
            # one full loop must be a multiple of 2. Without this line, more test cases fail. If you show up to a closed gate with 1,3,5... hours remaning, you have to go back and then forward again
            timeToKill = timeToKill + \
                1 if (timeToKill % 2 != 0) else timeToKill
            cost += prices[cheapestRoad] * timeToKill
            time += timeToKill


def calcCost(prices):
    retInt = 0
    for price in prices:
        retInt += price
    return retInt


main()
