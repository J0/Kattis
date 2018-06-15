inp = str(input())
arr = []
output = []
for cha in inp:
    arr.append(cha)
while(arr):
    print(arr[-1])
    count = 0
    while(arr[-1]=="<"):
        count += 1
        arr.pop()
    while(count > 0):
        arr.pop()
        count -= 1
    if arr[-1] != "<":
        output.append(arr[-1])
        arr.pop()
print(arr)
    
