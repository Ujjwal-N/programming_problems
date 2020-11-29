f = open("driver/1.in", "r")
lines = f.readlines()
tolls = str(lines[1]).split()
times = str(lines[2]).split()

for i in range(0, len(tolls)): 
    tolls[i] = int(tolls[i]) 
for i in range(0, len(times)): 
    times[i] = int(times[i]) 

roads = len(tolls)
toll = 0
gate = 0
time = 0

while(gate < roads):
	print("time: " + str(time))
	print("gate: " + str(gate))
	print("toll: " + str(toll))
	if(times[-1] < time):
		#print("here")
		
		toll += tolls[gate]
		gate += 1
		time += 1

	else:
		#print("hello")
		highestGate = gate
		for i in range(gate, roads):
			if(times[i] == times[highestGate]):
				print("here with i=" + str(i))
				highestGate = i

			if(time > times[i]):
				highestGate = i

		low = 0
		print("highestGate was found to be " + str(highestGate))
		for i in range(gate, (highestGate + 1)):
			print(i)
			if tolls[low] >= tolls[i]:
				low = i
		print("low was found to be " + str(low))
		while(gate != low):
			print("nG incrementing toll by " + str(tolls[gate]))
			toll += tolls[gate]
			gate += 1
			time += 1
		print("gate is now " + str(gate))
		dToll = tolls[gate]
		if((len(times) - 1) > highestGate):
			while (times[highestGate + 1] >= time):
				toll += dToll
				print("incrementing toll by " + str(dToll))
				if(gate == low):
					gate += 1
				elif (gate == (low+1)):
					print("decremented from " + str(gate))
					gate -= 1
				time += 1
		print()
print(toll)