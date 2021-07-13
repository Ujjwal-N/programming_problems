def main():
    inStr = input()
    wordLen = len(inStr)
    divThree = wordLen // 3
    one = inStr[: divThree]
    two = inStr[divThree: 2 * divThree]
    three = inStr[2 * divThree:]
    if(one == two):
        print(one)
    else:
        print(three)


main()
