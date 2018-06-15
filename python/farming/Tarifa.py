x = int(input())
n = int(input())
_sum = 0
for i in range(n):
  _sum+=int(input())
print(x * (n + 1) - _sum)
