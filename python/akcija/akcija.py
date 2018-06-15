numQueries = int(input())
arr = []
for i in range(numQueries):
  y = int(input())
  arr.append(y)
arr = sorted(arr)
print(*arr, sep = ' ')

