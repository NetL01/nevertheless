def countsort(n, res):
    lst = [0] * n
    for i in range(len(res)):
        lst[i] += i

    srt = []
    for i in range(len(lst)):
        cc = i
        print(cc)
        print(lst[i])
        srt.extend((int(cc) * int(lst[i])))

    print(*srt)

n = int(input())
res = list(map(int, input().split()))
print(res)
countsort(n, res)
