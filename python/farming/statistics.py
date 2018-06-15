from sys import stdin
lines = stdin.readlines()
for counter, line in enumerate(lines):
  inp = [int(x) for x in line.split()]
  del inp[0]
  print("Case %s: %s %s %s" %(counter + 1,min(inp), max(inp), max(inp) - min(inp)))



