test_cases = int(input())
for x in range(test_cases):
	blank_line = input()
	counter = 0
	lis = []
	lis1 = []
	lis2 = []
	a = [int(i) for i in input().split()]
	total_stud = a[0]+ a[1]
	lis1 = [int(l) for l in input().split()]
	lis2 = [int(z) for z in input().split()]
	avg1 = sum(lis1)/len(lis1)
	avg2 = sum(lis2)/len(lis2)
	for b in lis1:
		if b > avg2 and b <avg1:
			counter +=1
	print(counter)