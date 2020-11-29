import requests
from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join
from functools import cmp_to_key

URLstarter = 'https://open.kattis.com/problems/'
partialIDs = []
solvedIDs = []
probDiffs = {'tgif': 3.1, 'moscowdream': 1.9, 'kolone': 2.7, 'parking': 1.8, 'boatparts': 1.5, 'cokolada': 2.3, 'modulo': 1.4, 'marko': 1.8, 'keytocrypto': 1.8,
             'planina': 1.3, 'reconnaissance': 3.8, 'icpcteamselection': 2.8, 'knightjump': 2.4, 'decisions': 3.2, 'bard': 2.5, 'driver': 3.9, 'farey': 3.7}


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


createdSortedArrays()
print(probDiffs)
print(solvedIDs)
print(partialIDs)
