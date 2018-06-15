nodes = 1 
edges = 1 
while not nodes == 0 and not edges == 0:
	lis = []
	inp = [int(x) for x in input().split()]
	nodes = inp[0]
	edges = inp[1]
	for y in range(edges):
		lis.append([int(z) for z in input().split()])
	print(lis)	
