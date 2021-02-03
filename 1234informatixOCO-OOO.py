one = int(input()).split()
two = int(input()).split()
# 4 т.п => len(angles) = 4
angles = []

def ur1(x1, x2, y1, y2):
    ura1 = [y1 - y2, x2 - x1, x1*y2 - x2*y1]
    return ura1

def ur2(x1, x2, y1, y2):
    ura2 = [y1 - y2, x2 - x1, x1*y2 - x2*y1]
    return ura2

def ur3(x1, x2, y1, y2):
    ura3 = [y1 - y2, x2 - x1, x1*y2 - x2*y1]
    return ura3

def ur4(x1, x2, y1, y2):
    ura4 = [y1 - y2, x2 - x1, x1*y2 - x2*y1]
    return ura4

# 0 1   2 3   4 5

# 0 1 | 2 3 | 3 2
# 3 0 | 3 3 | 5 2

# получение уравнений прямых по точкам
urvv1 = ur1(one[0], one[2], one[1], one[3])
urvv2 = ur2(one[0], one[4], one[1], one[5])
urvv3 = ur3(two[0], two[2], two[1], two[3])
urvv4 = ur4(two[0], two[4], two[1], two[5])

# (a1 - a)x + (b1 - b)y + (c1 - c) = 0

7x + 5y + 2 = 0
