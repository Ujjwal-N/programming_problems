nVillagers = int(input())  # total number of villagers
# songKnowledgeSet[member] = song knowledge(nights they heard songs) set
songKnowledgeSet = {}
bard = []  # bard[night] returns whether the bard was present that night

for vID in range(nVillagers):
    songKnowledgeSet[vID] = set()

nNights = int(input())
nights = []  # nights[night] returns an array with all of the people present that night

for n in range(nNights):
    splitted = input().split()
    currNight = []
    bardC = False
    for i in range(1, len(splitted)):  # splitted array of all villagers in the current night
        member = int(splitted[i]) - 1  # -1 because of array indexing
        if(member == 0):
            bardC = True
        currNight.append(member)
    bard.append(bardC)
    nights.append(currNight)

for night in range(len(nights)):
    if(bard[night]):
        # if bard is present, the night gets added to everyone's songKnowledgeSet
        for member in nights[night]:
            songKnowledgeSet[member].add(night)
    else:  # if bard is not present that nigh
        for member in nights[night]:
            for otherMember in nights[night]:
                for song in songKnowledgeSet[member]:
                    songKnowledgeSet[otherMember].add(song)

for member in songKnowledgeSet:
    if(songKnowledgeSet[member] == songKnowledgeSet[0]):
        print(member + 1)
