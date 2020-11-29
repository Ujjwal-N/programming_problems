def main():
	num = int(input())
	sq = 2
	i = 0
	while(i < num):
		sq = 2*sq - 1
		i += 1
	print(sq*sq)
main()