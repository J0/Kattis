import sys 

def take_input():
	lis = []
	for i in sys.stdin.readlines():
		read = i.split()
		lis.append((int(read[0]),int(read[1])))	
	num_people = lis[0][0]
	time = lis[0][1]

take_input()

def knapsack():

