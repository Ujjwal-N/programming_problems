def main():
    lines = int(input())
    for i in range(lines):
        nums = [int(i) for i in input().split(" ")]
        wildCards = nums[3]
        nums = nums[0:3]
        nums.sort()
        high = -1

        if(wildCards <= 100):
            lowest = 0
            while(lowest <= wildCards):
                remainingCards = wildCards - lowest
                middle = 0
                while(middle <= remainingCards):
                    highest = remainingCards - middle
                    option = nums.copy()
                    option[0] += lowest
                    option[1] += middle
                    option[2] += highest
                    cSum = calcSum(option)
                    if(cSum > high):
                        high = cSum
                    middle += 1
                lowest += 1
            print(high)
            continue
        nums[2] += wildCards
        print(calcSum(nums))


def calcSum(nums):
    retInt = 0
    for num in nums:
        retInt += num * num
    nums.sort()
    return 7 * nums[0] + retInt


main()
