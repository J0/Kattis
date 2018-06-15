lis = []
for i in range(10):
	lis.append(int(input()) % 42)
print(len(set(lis)))