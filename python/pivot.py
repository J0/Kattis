num = int(input())
lis = [int(x) for x in input().split()]
min_num = lis[0]
max_num = 0
counter = 0
flag = 0



other_lis = []
final_lis = sorted(lis)
for a in range(len(lis)):
	if  lis[a] == final_lis[a]:
		min_num = lis[a]
		other_lis.append(min_num)
	elif lis[a] > final_lis[a]:
		min_num = final_lis[a]
		other_lis.append(min_num)
	else:
		other_lis.append(min_num)


for ele in enumerate(lis, start = 0):
	if max_num < ele[1]:
		max_num = ele[1] 
		if lis[ele[0]] == other_lis[ele[0]]:
			counter += 1
'''
#print(counter)
for j in range(len(lis)):
	other_lis.append(min(lis[j:]))

for ele in enumerate(lis, start = 1):
	if max_num < ele[1]:
		max_num = ele[1]
		for  j in range(ele[0], len(lis)):
			if lis[j] < max_num:
				flag = -1 
				break
		if flag != -1:
			counter +=1
	flag = 0
'''
print(counter)


