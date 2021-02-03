mat = [[1, 0, 3],
       [4, 0, 3],
       [7, 0, 2]]

m = 3
n = 3
resp = []
for i in range(len(mat)):
    maxx = 0
    for j in range(len(mat)):
        if maxx < mat[i][j]:
            maxx = mat[i][j]
    resp.append(maxx)

print(min(resp))
