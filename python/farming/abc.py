y = sorted( [ int(x) for x in input().split()])
j = input()
output = []
for i in j:
  if i == "A":
    output.append(str(y[0]))
  elif i == "B":
    output.append(str(y[1]))
  else:
    output.append(str(y[2]))
  
print(*output, sep=' ' )
#w = [j[z] for z in range(len(j))]
#res = sorted(zip(y,w), key=lambda x : x[1] )
#bla = ""
#for i in res:
#  bla += str(i[0])
#print(bla)
