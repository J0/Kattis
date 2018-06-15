
from collections import deque
import time
"""def fix(N):
    _list = [int(x) for x in N.split()]
    jack_disc = _list[0]
    jill_disc = _list[1]
    q = []
    oq = []
    q_counter = 0
    oq_counter = 0
    shared_discs = 0
    for count in range(jack_disc):
        x = int(input())
        q.append(x)
    for other_count in range(jill_disc):
        y = int(input())
        oq.append(y)
    while not ((q_counter == jack_disc) or (oq_counter == jill_disc)):
        if q[q_counter] == oq[oq_counter]:
            shared_discs += 1
            q_counter += 1
        elif q[q_counter] > oq[oq_counter]:
            oq_counter += 1
        else:
            q_counter += 1

    print(shared_discs)


N = input()

while True:
    if N != "0 0":
        fix(N)
        N = input()
    else:
        break"""
start = time.clock()

def code (N):
    jackjill = [int(x) for x in N.split(" ")]
    counter = 0
    jack = []
    jill = []
    while counter < jackjill[0]:
        q = int(raw_input ())
        jack.append (q)
        counter += 1
    counter = 0
    while counter < jackjill[1]:
        p = int(raw_input())
        jill.append (p)
        counter += 1
    jackcount = 0
    jillcount = 0
    cd = 0
    while not((jackcount == jackjill[0]) or (jillcount == jackjill[1])):
        if jack [jackcount] == jill [jillcount]:
            cd += 1
            jackcount += 1
        elif jack [jackcount] > jill [jillcount]:
            jillcount += 1
        else:
            jackcount += 1
    print cd

N = raw_input ()

while True:
    if N != "0 0":
        code (N)
        N = raw_input ()
    else:
        break
print(time.clock() - start)
