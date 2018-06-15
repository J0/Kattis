num_test_cases = input()
for i in range(int(num_test_cases)):
  x = input()
  if x == "P=NP":
    print("skipped")
    continue
  else:
    y = x.split("+")
    print(int(y[0]) + int(y[1]))
