lis = []
try:
	while True:
		x,y = input().strip().split(' ')
		lis.append((int(x),int(y)))
except EOFError:
	pass

for item in lis:
	print(abs(item[1]-item[0]))
