n = int(input())
res = list(map(int, input().split()))
num = int(input())
count = 0
for i in res:
    if int(i) == int(num):
        count += 1
print(count)
