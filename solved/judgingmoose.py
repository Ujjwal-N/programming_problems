def main():
    tines = input().split(" ")
    left = int(tines[0])
    right = int(tines[1])

    if(left == 0 and right == 0):
        print("Not a moose")
        return
    left *= 2
    right *= 2
    if(left == right):
        print("Even " + str(left))
    elif(left > right):
        print("Odd " + str(left))
    else:
        print("Odd " + str(right))


main()
