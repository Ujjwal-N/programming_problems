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
	move = [-1,-1]
	if(checkValidity(square, possMove[0], possMove[1])):
		move[0] = int(square[0]) + int(possMove[0])
		move[1] = int(square[1]) + int(possMove[1])
		if(board[move[0]][move[1]] != '#'):
			retArr.append(move)
	return retArr



def generateMoves(square):
	re = []
	move = [-1,-1]
	possMoves = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
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
	if(knightPos == [0,0]):
		print(0)
		return
	moves = 0
	nMoves = [knightPos]
	dMoves = [[0,0]]
	oldMovesN = 0
	while(not done):
		moves = moves + 1
		oldMovesD = len(dMoves)
		for i in range(oldMovesD):
			generatedMoves = generateMoves(dMoves[i])
			for ge in generatedMoves:
				if not(ge in dMoves):
					dMoves.append(ge)
					for n in range(oldMovesN, len(nMoves)):
						if(ge == nMoves[n]):
							print(moves)
							return
		moves = moves + 1
		oldMovesN = len(nMoves)
		for i in range(oldMovesN):
			generatedMoves = generateMoves(nMoves[i])
			for ge in generatedMoves:
				if not(ge in nMoves):
					nMoves.append(ge)
					for n in range(oldMovesD, len(dMoves)):
						if(ge == dMoves[n]):
							print(moves)
							return

		if(len(dMoves) == oldMovesD or len(nMoves) == oldMovesN):
			print(-1)
			done = True
			return

		if(moves > 1000):
			print("fuck")
			done = True
			return 

main()