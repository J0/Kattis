import sys
'''
Take in an array with input symbols

'''
num = '1234567890'
def notation(arr):
	result = 0
	print(arr)
	for i in range(len(arr) - 1):
		if arr[i] in num and arr[i + 1] in num:
			result = int(arr[i]) + int(arr[i + 1])
	return str(result) 


for x in sys.stdin:
	arr = []
	arr.extend(x.strip("\n").split(" "))
	print("Case 1:" + notation(arr))

