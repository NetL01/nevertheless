mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

resp = []
k = int(input())
for i in range(len(mat)):
    resp.append(mat[i][k])
umn = 1
summ = 0
for i in resp:
    umn = umn * i
for i in resp:
    summ = summ + i
    
print(umn)
print(summ)
    
