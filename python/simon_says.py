cases = input()
store = []
for i in range(int(cases)):
    statement = input()
    store.append(statement)
    simon = "simon says "
for j in range(len(store)):
    if simon in store[j]:
        print(store[j].split(simon)[1])
    else:
        print()
        
