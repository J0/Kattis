test_case = input().split()
for i in range(1, int(test_case[2]) + 1):
  x = int(test_case[0])
  y = int(test_case[1])
  if i % x == 0 and i % y ==0:
    print("FizzBuzz")
  elif i % x == 0:
    print("Fizz")
  elif i % y == 0:
    print("Buzz")
  else:
    print(i)

