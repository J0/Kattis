lis = [int(x)for x in input().split()]
kings = 1 - lis[0]
queens = 1 - lis[1]
rooks = 2 - lis[2]
bishops = 2 - lis[3]
knights = 2 - lis[4]
pawns = 8 - lis[5]
print(kings, queens, rooks, bishops, knights, pawns)
