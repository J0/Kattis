s = input()
y = [int(x) for x in input().split()]
counter = 0
for a in y:
	if a<0:
		counter+=1
print(counter)