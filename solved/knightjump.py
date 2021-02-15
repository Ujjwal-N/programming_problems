board = []
squares = 0


def checkValidity(square, row, column):
    global squares
    rowOk = False
    columnOk = False
    if(row > 0):
        rowOk = (squares - row) >= square[0]
    else:
        rowOk = (-1 * row) <= square[0]
    if(column > 0):
        columnOk = (squares - column) >= square[1]
    else:
        columnOk = (-1 * column) <= square[1]
    return (rowOk and columnOk)


def returnMoves(square, possMove):
    retArr = []
    move = [-1, -1]
    if(checkValidity(square, possMove[0], possMove[1])):
        move[0] = int(square[0]) + int(possMove[0])
        move[1] = int(square[1]) + int(possMove[1])
        if(board[move[0]][move[1]] == '.'):
            board[move[0]][move[1]] = "T"
            retArr.append(move)
    return retArr


def generateMoves(square):
    re = []
    move = [-1, -1]
    possMoves = [[2, 1], [2, -1], [-2, 1], [-2, -1],
                 [1, 2], [1, -2], [-1, 2], [-1, -2]]
    for possMove in possMoves:
        returnedMoves = returnMoves(square, possMove)
        if(len(returnedMoves) == 1):
            re.append(returnedMoves[0])
    return re


def main():
    global board
    global squares
    num = int(input())
    knightPos = []
    for i in range(num):
        inp = input()
        splitted = [i for i in inp]
        if('K' in splitted):
            knightPos.append(i)
            knightPos.append(splitted.index('K'))
        board.append(splitted)
    squares = num - 1
    done = False
    if(knightPos == [0, 0]):
        print(0)
        return
    moves = 0
    kMoves = [knightPos]
    while(not done):
        moves += 1
        if(moves > 100):
            print(-1)
            return
        nextSet = []
        while(len(kMoves) != 0):
            poppedMove = kMoves.pop()
            currMoves = generateMoves(poppedMove)
            for cMove in currMoves:
                if(cMove == [0, 0]):
                    print(moves)
                    return
                nextSet.append(cMove)
        kMoves = nextSet


main()
