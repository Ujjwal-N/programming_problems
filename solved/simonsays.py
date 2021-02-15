nums = int(input())
for i in range(nums):
    line = input()
    if (line[0:11] == "Simon says "):
        print(line[11:])
