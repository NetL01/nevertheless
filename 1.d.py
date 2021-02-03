strr = [c for c in input()]
num = int(input())
count = 0
for i in range(len(strr)):
    if int(strr[i]) == int(num):
        count += 1
if count != 0:
    print('YES')
else:
    print('NO')
