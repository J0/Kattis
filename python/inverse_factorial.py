import math
fac = input()
dic = {}
counter = 0
i = 1	
if fac == '1':
	print(1)
if fac == '2':
	print(2)
if fac == '120':
	print(5)
if fac =='720':
	print(6)
if fac != '720' and fac != '2' and fac!='1' and fac!='120':	
	while(counter < 10**6):
		counter += math.log(i, 10)
		floored = math.floor(counter)+1
		dic[floored] = i
		i = i + 1
	print(dic[len(fac)])




'''
'''