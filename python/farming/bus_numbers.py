import re
import sys
num_buses = int(input())
lis = [int(x) for x in input().split()]
sorted_lis = sorted(lis)
other_lis = []
output = ""
if len(sorted_lis) == 1:
  print(sorted_lis[0])
  sys.exit(0)
else:
  if sorted_lis[1] - sorted_lis[0] ==1:
    other_lis.append(sorted_lis[0])
  else:
    output += str(sorted_lis[0])
  for index in range(1, len(sorted_lis)):
    if sorted_lis[index] - sorted_lis[index - 1] == 1:
      other_lis.append(sorted_lis[index])
    else:
      if len(other_lis) > 2:
        output += "{}-{} ".format(other_lis[0], other_lis[-1])
        other_lis = []
        other_lis.append(sorted_lis[index])
      else:
        other_lis.append(sorted_lis[index])
        for item in other_lis:
          output += (" " + str(item))
        other_lis = []
print(other_lis)
if other_lis:
  if len(other_lis) > 2:
    output += "{}-{}".format(other_lis[0], other_lis[-1])
  else:
    for item in other_lis:
      output += (" " + str(item))
print(re.sub("\s+", " ", output))
