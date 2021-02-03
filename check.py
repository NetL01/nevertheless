m = (map(int, input().split()) for _ in range(int(input())))
a = {frozenset([ci+1, ni+1]) for ni, ne in enumerate(m) for ci, ce in enumerate(ne) if ce == 1}
print(len(a))
