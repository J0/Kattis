num_test_cases = int(input())

for i in range(num_test_cases):
  x = input()
  print(x)
  se = set()
  while(x !="what does the fox say?"):
    if x.split()[1] == "goes":
      se.add(x.split()[0])
      se.add(x.split()[2])
    else:
      se.add(y for y in x.split())
print(se)


      
    
