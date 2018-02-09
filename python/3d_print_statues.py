test = int(input())
total = 0
for i in range(1, test + 1):
	total += i
	if total > test:
		print(test - 1)	
		break
	elif total == test:
		print(test)