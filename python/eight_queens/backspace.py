line = [x for x in input()]
output = []
while line:
    count = 0
    while line[-1] == "<":
        line.pop()
        count +=1
    for counter in range(count):

        line.pop()

    if line and line[-1] is not "<":
        output.append(line.pop())
output.reverse()
print(*output, sep = '')
