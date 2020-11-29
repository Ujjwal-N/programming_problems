import requests
from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join
from functools import cmp_to_key

URLstarter = 'https://open.kattis.com/problems/'
partialIDs = []
solvedIDs = []
probDiffs = {}


def extractDifficulty(itemID):
    global URLstarter
    URL = URLstarter + itemID
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    sidebar = soup.find_all('p')
    matchStr = "<p><strong>Difficulty:  </strong><span>"
    startIndex = len(matchStr)
    endIndex = len(matchStr) + 3
    for item in sidebar:
        stringMaybe = str(item)
        if(stringMaybe.startswith(matchStr)):
            return float(stringMaybe[startIndex:endIndex])
            break


def sortByDifficulty(problemIDs):
    for problemID in problemIDs:
        if not(problemID in probDiffs):
            probDiffs[problemID] = extractDifficulty(problemID)
    return sorted(problemIDs, key=cmp_to_key(compareProblems))


def compareProblems(item1, item2):
    diff1 = probDiffs[item1]
    diff2 = probDiffs[item2]
    if(diff1 < diff2):
        return 1
    elif(diff1 == diff2):
        return 0
    else:
        return -1


def readFiles():
    global solvedIDs
    global partialIDs
    solvedPath = "/Users/ujjwalnadhani/Desktop/programming_problems/solved"
    solvedIDs = extractProblems(solvedPath)
    partialPath = "/Users/ujjwalnadhani/Desktop/programming_problems/partial"
    partialIDs = extractProblems(partialPath)
    readDiffFile()


def readDiffFile():
    global probDiffs
    with open("diff.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            splitted = line.strip("\n").split(',')
            if(len(splitted) == 2):
                probDiffs[splitted[0]] = float(splitted[1])


def writeDiffFile():
    with open("diff.txt", "w") as f:
        f.seek(0)
        for key in probDiffs:
            f.write(key + "," + str(probDiffs[key]) + "\n")
        f.truncate()


def extractProblems(mypath):
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    retStr = []
    for f in onlyfiles:
        if(f[0] != '.'):
            currChar = f[0]
            currStr = ""
            i = 0
            while(currChar != '.'):
                currStr += str(currChar)
                i += 1
                currChar = f[i]
            retStr.append(currStr)
    return retStr


def createdSortedArrays():
    global solvedIDs
    global partialIDs
    readFiles()
    solvedIDs = sortByDifficulty(solvedIDs)
    partialIDs = sortByDifficulty(partialIDs)
    writeDiffFile()


def updateReadMe():
    global solvedIDs
    global partialIDs
    createdSortedArrays()
    with open("README.md", "r") as f:
        lines = f.readlines()
    with open("README.md", "w") as f:
        f.seek(0)
        for line in lines:
            if not(line.startswith("## Problems Solved Completely")):
                f.write(line)
            else:
                break
        f.truncate()
        f.write("## Problems Solved Completely(" + str(len(solvedIDs)) + ")\n")
        for sID in solvedIDs:
            printStr = "* [" + sID + "](" + URLstarter + sID + "), difficulty: " + \
                str(probDiffs[sID]) + "\n"
            f.write(printStr)
        f.write("## Problems Solved Partially(" + str(len(partialIDs)) + ")\n")
        for pID in partialIDs:
            printStr = "* [" + pID + "](" + URLstarter + pID + "), difficulty: " + \
                str(probDiffs[pID]) + "\n"
            f.write(printStr)
        f.write("\n")
        f.write(
            "The problems in the \"partially solved list\" will move to the \"completely solved list\" eventually...")


updateReadMe()
