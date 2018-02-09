test_case = int(input())
access_and_houses = [int(x) for x in input().split()]
access_points = access_and_houses[0]
num_houses = access_and_houses[1]
lis = []
for y in range(num_houses):
	lis.append(int(input()))
print(lis)