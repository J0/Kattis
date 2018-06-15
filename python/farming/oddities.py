inp = input()
z = []
for i in range(int(inp)):
    z.append(int(input()))
for b in z:
    if b % 2 ==0:
        print(str(b) + " is even")
    else:
        print(str(b) + " is odd")
    
