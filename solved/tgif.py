def main():

	lineOne = input().split()
	calendarDay = int(lineOne[0])
	month = lineOne[1]
	weekday = input()
	
	days = convertToDays(calendarDay, month)
	res = obtainDesiredModulo(weekday)
	if(days <= 59):
		if(days % 7 == res):
			print("TGIF")
		else:
			print(":(")
	else:
		poss1 = days % 7
		days += 1
		poss2 = days % 7
		if(poss1 == res or poss2 == res):
			print("not sure")
		else:
			print(":(")


def convertToDays(calendarDay, month):
	monthToDays = {
		"JAN": 31, 
		"FEB": 28, 
		"MAR": 31,
		"APR": 30,
		"MAY": 31,
		"JUN": 30,
		"JUL": 31,
		"AUG": 31,
		"SEP": 30,
		"OCT": 31,
		"NOV": 30,
		"DEC": 31
	}

	retVal = 0
	for i in monthToDays.keys():
		if(i == month):
			break
		else:
			retVal += monthToDays[i]
	return calendarDay + retVal - 1


def obtainDesiredModulo(weekday):
	daysArray = ["SUN","MON", "TUE", "WED", "THU", "FRI", "SAT"]
	currentDay = weekday
	retVal = 0
	i = daysArray.index(weekday)
	while(currentDay != "FRI"):
		retVal += 1
		if(i >= 6):
			i = 0
		else:
			i += 1
		currentDay = daysArray[i]
	return retVal


main()

