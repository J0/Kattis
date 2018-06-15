num = int(input())
score = 0
counter = 0
lis = [int(x) for x in input().split()]
for i in range(num):
  x = lis[i]
  if x != -1:
    score += x
    counter +=1
print(score/counter)
