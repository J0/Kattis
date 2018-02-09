autori = raw_input()
lis = autori.split('-')
result = ""
for item in lis:
	result += item[0]
print(result)
