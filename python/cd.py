while True:
	x = input().split()
	jack_cds = int(x[0])
	jill_cds = int(x[1])
	a = []
	b = [] 
	if jack_cds == 0  and jill_cds == 0:
		break
	for i in range(jack_cds):
		a.extend(input())
	for j in range(jill_cds):
		b.extend(input())
	x = [c for c in a if c in b]
	print(len(x))
