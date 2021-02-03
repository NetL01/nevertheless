def vert(matrix):
    n = len(matrix)
    for i in range(n):
        q = 0
        for j in range(n):
            q += abs(matrix[i][j])
        if q == 0:
            return 'YES'
    return 'NO'

# n = int(input())
# m = [n][m]
# for i in range(n):
#    x = list(map(int, input().split()))
#    m.append(x)

n = int(input())
s = []
for i in range(n):
    res = list(map(int, input().split()))
    s.append(res)

mz = [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
print(vert(s))
