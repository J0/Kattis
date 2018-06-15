num_cases = int(input())
for i in range(num_cases):
    output = ""
    a = input()
    b = input()
    for c in range(len(a)):
      if a[c] == b[c]:
        output+= "."
      else:
        output+= "*"
    print(a)
    print(b)
    print(output)
    print("\n")       
