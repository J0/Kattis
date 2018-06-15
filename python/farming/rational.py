from fractions import Fraction
num_cases = int(input())
for i in range(num_cases):
  arr = input().split()
  nume_one = int(arr[0])
  denom_one = int(arr[1])
  nume_two = int(arr[3])
  denom_two = int(arr[4])
  operator = arr[2]
  if operator == "+":
    result = Fraction(nume_one, denom_one) + Fraction(nume_two, denom_two)
  elif operator == "-":
    result = Fraction(nume_one, denom_one) - Fraction(nume_two, denom_two)
  elif operator == "*":
    result = Fraction(nume_one, denom_one) * Fraction(nume_two, denom_two)
  elif operator == "/":
    result = Fraction(nume_one, denom_one) / Fraction(nume_two, denom_two)
  print(str(result.numerator) + " / " + str(result.denominator))

