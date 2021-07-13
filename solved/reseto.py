def main():
    inps = [int(i) for i in input().split(" ")]
    n = inps[0]
    k = inps[1]

    nums = [False] * (n - 1)
    nums.insert(0, True)
    nums.insert(0, True)
    i = 0
    done = False
    while(not done):
        dNum = -1
        for j in range(2, (n + 1)):
            if(not nums[j]):
                dNum = j
                break
        if(dNum == -1):
            break
        nums[dNum] = True
        i += 1
        if(i == k):
            print(dNum)
            break
        l = dNum * 2
        while(l < (n + 1)):
            if(not nums[l]):
                nums[l] = True
                i += 1
                if(i == k):
                    print(l)
                    done = True
                    break
            l += dNum


main()
