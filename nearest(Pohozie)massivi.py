k = int(input())
srt = [x for x in input()]
srt.sort()
srt1 = set(srt)
j = int(input())
ptt = [x for x in input()]
ptt.sort()
ptt1 = set(ptt)
print(srt1, ptt1)
if ptt1 == srt1:
    print('YES')
else:
    print('NO')
