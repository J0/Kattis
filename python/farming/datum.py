from datetime import datetime as dt
x = input().split()
date = x[0]+"-" + x[1]+"-2009"
a = dt.strptime(date, "%d-%m-%Y").weekday()
if a == 0:
  print("Monday")
elif a == 1:
  print("Tuesday")
elif a == 2:
  print("Wednesday")
elif a ==3 :
  print("Thursday")
elif a ==4:
  print("Friday")
elif a ==5:
  print("Saturday")
elif a ==6:
  print("Sunday")
