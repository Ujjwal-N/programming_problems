paths = []


def main():
    originalGrid = []
    red = []
    green = []
    blue = []
    yellow = []
    for i in range(4):
        currLine = input()
        for j in range(4):
            if(currLine[j] == "R"):
                red.append([i, j])
            elif(currLine[j] == "G"):
                green.append([i, j])
            elif(currLine[j] == "B"):
                blue.append([i, j])
            elif(currLine[j] == "Y"):
                yellow.append([i, j])
        originalGrid.append([char for char in currLine])
    colorsNotDone = []

    findAllPossiblePaths("R", originalGrid, red[0], red[1])
    redPaths = []
    if(len(paths) == 0):
        print("unsolvable")
        return
    else:
        originalGrid = findAndUpdateCriticalPoints("R", originalGrid)
        if(len(paths) > 1):
            colorsNotDone.append("R")
            redPaths = copy3DArray(paths)
    # only red works for some reason :(
    findAllPossiblePaths("G", originalGrid, green[0], green[1])
    greenPaths = []
    if(len(paths) == 0):
        print("unsolvable")
        return
    else:
        originalGrid = findAndUpdateCriticalPoints("G", originalGrid)
        if(len(paths) > 1):
            colorsNotDone.append("G")
            greenPaths = copy3DArray(paths)

    findAllPossiblePaths("B", originalGrid, blue[0], blue[1])
    bluePaths = []
    if(len(paths) == 0):
        print("unsolvable")
        return
    else:
        originalGrid = findAndUpdateCriticalPoints("B", originalGrid)
        if(len(paths) > 1):
            colorsNotDone.append("B")
            bluePaths = copy3DArray(paths)

    if(len(yellow) == 2):
        findAllPossiblePaths("Y", originalGrid, yellow[0], yellow[1])
        yellowPaths = []
        if(len(paths) == 0):
            print("unsolvable")
            return
        else:
            originalGrid = findAndUpdateCriticalPoints("Y", originalGrid)
            if(len(paths) > 1):
                colorsNotDone.append("Y")
                yellowPaths = copy3DArray(paths)


def findAllPossiblePaths(color, grid, startingPoint, endingPoint):
    paths.clear()
    recursiveDFS(color, copy2DArray(grid), startingPoint[0], startingPoint[1],
                 endingPoint[0], endingPoint[1], [])


def recursiveDFS(color, grid, startX, startY, endX, endY, path):
    newPath = copy2DArray(path)
    newGrid = copy2DArray(grid)
    if(startX == endX and startY == endY):
        paths.append(newPath)
    else:
        if(startX > 0):
            if(grid[startX - 1][startY] == "W" or ((startX - 1) == endX and startY == endY)):
                newPath.append([startX - 1, startY])
                newGrid[startX - 1][startY] = color
                recursiveDFS(color, newGrid, startX - 1,
                             startY, endX, endY, newPath)
                newPath = path
                newGrid = grid
        if(startX < 3):
            if(grid[startX + 1][startY] == "W" or ((startX + 1) == endX and startY == endY)):
                newPath.append([startX + 1, startY])
                newGrid[startX + 1][startY] = color
                recursiveDFS(color, newGrid, startX + 1,
                             startY, endX, endY, newPath)
                newPath = path
                newGrid = grid
        if(startY > 0):
            if(grid[startX][startY - 1] == "W" or (startX == endX and (startY - 1) == endY)):
                newPath.append([startX, startY - 1])
                newGrid[startX][startY - 1] = color
                recursiveDFS(color, newGrid, startX,
                             startY - 1, endX, endY, newPath)
                newPath = path
                newGrid = grid
        if(startY < 3):
            if(grid[startX][startY + 1] == "W" or (startX == endX and (startY + 1) == endY)):
                newPath.append([startX, startY + 1])
                newGrid[startX][startY + 1] = color
                recursiveDFS(color, newGrid, startX,
                             startY + 1, endX, endY, newPath)
                newPath = path
                newGrid = grid


def findAndUpdateCriticalPoints(color, grid):
    newGrid = copy2DArray(grid)
    firstPath = paths[0]
    for potPoint in firstPath:
        notFound = False
        for fullPath in paths:
            if(not potPoint in fullPath):
                notFound = True
                break
        if(not notFound):
            newGrid[potPoint[0]][potPoint[1]] = color
    return newGrid


def copy2DArray(inp):
    retVar = []
    for elem in inp:
        retVar.append(elem.copy())
    return retVar


def copy3DArray(inp):
    retVar = []
    for elem in inp:
        retVar.append(copy2DArray(elem))
    return retVar


main()
