import random

mat = [[1, 2, 3, 5],
       [6, 7, 8, 7],
       [11, 12, 13, 4],
       [1, 2, 3, 9]]
# m = len(mat)
# for i in range(m):
#    for j in range(i + 1):
#        mat[i][j] = 0
# for y in range(m):
#    for x in range(m - y):
#        mat[y][x] = 0
# print(*mat, sep='\n')

for i in range(len(mat)//2):
    for j in range(i + 1):
        mat[len(mat)-i-1][j] = 0
print(*mat, sep='\n')
    
