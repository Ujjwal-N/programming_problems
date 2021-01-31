def main():
    dogTimes = [int(x) for x in input().split(" ")]
    dog1A = dogTimes[0]
    dog1C = dogTimes[1]
    dog2A = dogTimes[2]
    dog2C = dogTimes[3]

    peopleTimes = [int(x) for x in input().split(" ")]
    for person in peopleTimes:
        count = 0
        dog1Mod = person % (dog1A + dog1C)
        dog2Mod = person % (dog2A + dog2C)
        dog1Mod = (dog1Mod) if (dog1Mod != 0) else (dog1A + dog1C)
        dog2Mod = (dog2Mod) if (dog2Mod != 0) else (dog2A + dog2C)
        if(dog1Mod <= dog1A):
            count += 1
        if(dog2Mod <= dog2A):
            count += 1
        if(count == 0):
            print("none")
        elif(count == 1):
            print("one")
        else:
            print("both")


main()
