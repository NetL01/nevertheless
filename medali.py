n = int(input())
line = input()
max1 = 0
max2 = 0
for i in range(n*2):
    if (line[i] != ' ') and (int(line[i]) > max1):
        max1 = i
        if max1 > max2:
            max2 = max1
print(max2)
