def main():
    numTaps = int(input())
    temperature = []
    minFlowRate = []
    maxFlowRate = []
    for _ in range(numTaps):
        values = [int(i) for i in input().split(" ")]
        temperature.append(values[0])
        minFlowRate.append(values[1])
        maxFlowRate.append(values[2])
    numRecipes = int(input())
    for _ in range(numRecipes):
        line = [int(i) for i in input().split(" ")]
        dTemp = line[0]
        dFlow = line[1]
        dS = dTemp * dFlow
        done = False
        for i in range(numTaps):
            intercept = dS / temperature[i]
            # check if 0->intercept is in range of minFlow-maxFlow
            if(intercept < minFlowRate[i] or intercept > maxFlowRate[i]):
                print("no")
                done = True
                break
        if(not done):
            print("yes")


main()
