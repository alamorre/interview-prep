a = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]
b = [
    [1,1,1],
    [0,1,0],
    [0,0,1],
]
# c = [
#     [1, 3, 4],
#     [4, 9, 10],
#     [7, 15, 16],
# ]

# For each of a rows
#   for each of b's columns
#       sum product for each cell
# O(N^3) in time O(N^2) in space


# Assuming the matricies are valid i.e. len(a[0]) == len(b)
c = []
for i, row in enumerate(a):
    new_row = []
    for j in range(0, len(b)):
        cell = 0
        for k in range(0, len(row)):
            cell += row[k] * b[k][j]
        new_row.append(cell)
    c.append(new_row)

import pprint
pprint.pprint(c)
