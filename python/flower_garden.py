import sys
test_cases = input()
lis = []
for i in sys.stdin:
    ab = i.split()
    a = int(ab[0])
    b = int(ab[1])
    lis.append((a,b))
print(test_cases)
print(lis)
print(num_flowers)
