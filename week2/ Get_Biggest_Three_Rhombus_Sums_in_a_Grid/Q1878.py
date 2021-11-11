# problem: only can go straight, can not backtrack.
grid = [
    [3,4,5,1,3],
    [3,3,4,2,3],
    [20,30,200,40,10],
    [1,5,5,4,1],
    [4,3,2,2,5]
]
rows_num = len(grid[0])
columns_num = len(grid)
target_grid = []
sum_num = []
for column in range(columns_num):
    for row in range(rows_num):
        aim_grid = []
        target_grid_dl = []
        target_grid_dr = []
        target_grid_ur = []
        target_grid_ul = []
        target_column = column
        target_row = row
        # look down left
        while target_column < columns_num and target_row >= 0:
            target_grid_dl.append(grid[target_column][target_row])
            target_column += 1
            target_row -= 1
        if len(target_grid_dl) == 1:
            target_grid.append(target_grid_dl)
            continue
        # get the max length target
        max_target_length = len(target_grid_dl)
        # get back the value
        target_row += 1
        target_column -= 1
        # look down right
        target_column += 1
        target_row += 1
        while target_column < columns_num and target_row < rows_num and len(target_grid_dr) < max_target_length - 1:
            target_grid_dr.append(grid[target_column][target_row])
            target_column += 1
            target_row += 1
        # get back the value
        target_row -= 1
        target_column -= 1
        # look up right
        target_column -= 1
        target_row += 1
        while target_column >= 0 and target_row < rows_num and len(target_grid_ur) < max_target_length - 1 :
            target_grid_ur.append(grid[target_column][target_row])
            target_column -= 1
            target_row += 1
        # get back the value
        target_row -= 1
        target_column += 1
        # look up left
        target_column -= 1
        target_row -= 1
        while target_column >= 0 and target_row >= 0 and len(target_grid_ul) < max_target_length - 1:
            target_grid_ul.append(grid[target_column][target_row])
            target_column -= 1
            target_row -= 1
        # merge target grid:
        if len(target_grid_dl) - 1 == len(target_grid_dr) == len(target_grid_ul) == len(target_grid_ur):
            aim_grid = target_grid_dl + target_grid_dr + target_grid_ur + target_grid_ul[:-1]
            target_grid.append(aim_grid)
for i in target_grid:
    sum_num.append(sum(i))
sum_num.sort()
print(sum_num[-3:])

