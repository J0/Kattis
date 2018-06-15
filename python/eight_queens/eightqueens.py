_list = [[x for x in range(8)] for y in range(8)]
flag = 0
def check_attacking(row, column):
    for counter in range(8):
        if _list[row][counter] == "*" and counter != column :
            return True
        elif _list[counter][column] == "*" and row != counter:
            return True
        # Now check the diagonal
    other_counter = 1
    while row + other_counter < 8 and column + other_counter < 8:
        if _list[row + other_counter][column + other_counter] == "*":

            return True
        other_counter = other_counter + 1
    other_counter = 1
    while row - other_counter >= 0 and column - other_counter >= 0:
        if _list[row - other_counter][column - other_counter] == "*":
            return True
        other_counter = other_counter + 1
    #Need to check the back diagonal
    other_counter = 1
    while row - other_counter >= 0 and column + other_counter < 8:
        if _list[row - other_counter][column - other_counter] == "*":
            return True
        other_counter = other_counter + 1
    other_counter = 1
    while row + other_counter < 8 and column - other_counter >=0:
        if _list[row - other_counter][column - other_counter] == "*":
            return True
        other_counter = other_counter + 1
    return False

for counter in range(8):
    _list[counter] = input()
    for row in range(8):
        for column in range(8):
            if _list[row][column] == "*":
                if (check_attacking(row, column)):
                    flag = 1
if flag == 1:
    print("invalid")
else:
    print("valid")
