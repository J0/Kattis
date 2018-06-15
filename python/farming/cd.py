while True:
    x = input().split()
    jack_cds = int(x[0])
    jill_cds = int(x[1])
    a = set()
    b = set()
    _max = 0
    if jack_cds == 0 and jill_cds == 0:
        break
    for i in range(jack_cds):
        ay = int(input())
        a.add(ay)
        if ay > _max:
            _max = ay
    for j in range(jill_cds):
        jy = int(input())
        if jy > _max:
            continue
        b.add(jy)
    print(len(a & b))
