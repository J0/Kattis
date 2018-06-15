import sys
lis = []
for i in range(9):
  x = int(input())
  lis.append(x)

for num in range(9):
  temp = lis[num]
  lis[num] = 0
  for other_num in range(num + 1,9):
    tempa = lis[other_num]
    lis[other_num] = 0
    if sum(lis) == 100:
      lis = filter(lambda x : x!=0, lis)
      print(*lis, sep='\n')
      sys.exit(0)
    else:
      lis[other_num] = tempa
  lis[num] = temp
