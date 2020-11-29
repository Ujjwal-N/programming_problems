
nVillagers = int(input()) #total number of villagers
songKnowledge = [] #songKnowledge[member] = total number of songs they know
bard = [] #bard[night] returns whether the bard was present that night

for _ in range(nVillagers):
	songKnowledge.append(0)

nNights = int(input())
nights = [] #nights[night] returns an array with all of the people present that night

for n in range(nNights):
	splitted = input().split()
	currNight = []
	bardC = False
	for i in range(1,len(splitted)): #splitted array of all villagers in the current night
		member = int(splitted[i]) - 1 #-1 because of array indexing
		if(member == 0):
			bardC = True
		currNight.append(member)
	bard.append(bardC)
	nights.append(currNight)

for night in range(len(nights)):
	if(bard[night]):
		for member in range(len(nights[night])): #if bard is present, everyone's song knowledge increases by one
			curr = nights[night][member]
			songKnowledge[curr] += 1
	else: #if bard is not present that night
		
		high = -1
		totalPeople = len(nights[night])
		for person in range(totalPeople): #find the person who knows the most songs tonight and save all the songs they know
			curr = nights[night][person]
			currK = songKnowledge[curr]
			if (high < currK):
				high = currK
		
		for member in range(totalPeople):
			curr = nights[night][member]
			songKnowledge[curr] = high #everyone in the village except bard knows all of these songs

print(bard)
print(nights)
print(songKnowledge)
maxSongs = songKnowledge[0]
for song in songKnowledge:
	if(song > maxSongs):
		maxSongs = song

for songIndex in range(0, len(songKnowledge)):
	if(songKnowledge[songIndex] == maxSongs):
		print(songIndex + 1)

