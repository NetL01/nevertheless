n = int(input())
lis = []
for i in range(n):
    asq = list(map(int, input().split()))
    lis.append(asq)
cout1 = 0
for i in asq:
    if i == '1':
        cout1 += 1
print(cout1)
