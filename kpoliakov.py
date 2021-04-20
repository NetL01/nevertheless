count = 0
with open('27-17b.txt') as f:
    n = int(f.readline())
    m = list(map(int, f.readlines()))
    for i in range(0, n-5):
        for j in range(i+5, n):
            if (m[i] + m[j]) % 2 == 1 and (m[i] * m[j]) % 13
                count += 1
print(count)
