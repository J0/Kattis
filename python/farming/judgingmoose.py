x, y = input().split()
x = int(x)
y = int(y)
if x==0 and y==0:
  print("Not a moose")
elif x == y:
  print("Even %s" %(x*2))
elif x > y :
  print("Odd %s" %(x*2))
else:
  print("Odd %s" %(y*2))
