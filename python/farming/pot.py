num_input = int(input())
lis = []
for x in range(num_input):
	lis.append(input())
output = 0
for y in lis:
	output += int(y[:-1]) **int(y[-1])
print(output)