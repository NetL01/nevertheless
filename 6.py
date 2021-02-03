mat = [[7, 2, 3],
       [4, 5, 6],
       [1, 8, 9]]
resp = []
for i in range(len(mat)):
    resp.append(mat[i][0])
resp.sort()
for i in range(len(mat)):
    mat[i][0] = resp[i]
print(mat)
        
