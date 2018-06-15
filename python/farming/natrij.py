s = input()
other=  input()
d,m,y = s.split(":")
d2,m2,y2 = other.split(":")

d3 = int(d2) - int(d)
m3 = int(m2) - int(m)
y3 = int(y2) - int(y)
if y3 <0 :
  y3 =60 + y3
if m3 <0:
  m3 = 60 + m3
if d3 <0:
  d3 = 24 + d3
print("%02d:%02d:%02d" %(d3,m3,y3))
