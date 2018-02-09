from collections import *
participants = int(input())
arr = [int(x) for x in input().split()]
c = Counter(arr)
lis = []
for i in c.most_common():
	if i[1] == 1:
		lis.append(i)
if lis != []:
	test = max(lis)[0]
	for y in enumerate(arr, start = 0):
		if y[1] ==test:
			print(y[0] + 1)
			exit()
print("none")
