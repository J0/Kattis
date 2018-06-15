import sys
x = int(input())
def sorting(x):
	if x==0:
		quit()
	for i in range(x):
		lis.append(input())
	print(*sorted(lis, key= lambda lis:lis[:2]), sep = '\n')
	print("\n")
while(x!=0):
	lis =[]
	sorting(x)	
	x = int(input())
