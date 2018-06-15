arr = []
arr = input().split(' ')
H = int(arr[0])
directions = arr[1]
index = 1
maxheight= 2**(H+1)
for c in directions:
  if c=="L":
    index *= 2
  elif c =="R":
    index = index * 2 +1 

print(maxheight - index)
    
