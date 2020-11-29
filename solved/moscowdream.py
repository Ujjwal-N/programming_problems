def main():

	nums = input().split()
	tot = 0
	for i in range(0, 3):
		curr = int(nums[i])
		if(curr < 1):
			print("NO")
			return
		tot += curr
	problems = int(nums[3]) 
	if(tot <  problems or problems < 3):
		print("NO")
		return
	print("YES")
main()