x = input()
starting_pos = x[0]
rest_seats = x[1:]
arr = []
arr.append(starting_pos)
if starting_pos == "U" and rest_seats[0] == "U":
  policy_one = 0
  policy_two = -1
elif starting_pos == "D" and rest_seats[0] == "U":
  policy_one = 1
  policy_two = 0
elif starting_pos == "U" and rest_seats[0] == "D":
  policy_one = 0
  policy_two = 1
else:
  policy_one = -1
  policy_two = 0
# Policy one 
for i in rest_seats:
  if i == "D":
    policy_one += 2
# Policy two
for i in rest_seats:
  if i == "U":
    policy_two +=2
print(policy_one)
print(policy_two)

# Policy Three
for i in rest_seats:
  if i != arr[-1]:
    arr.append(i)
print(len(arr) - 1)
 

