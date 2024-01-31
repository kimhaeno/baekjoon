n = int(input())
xmin = 10000
xmax = -10000
ymin = 10000
ymax = -10000


for i in range(n):
    a, b = map(int, input().split())
    if a > xmax:
        xmax = a
    if a < xmin:
        xmin = a
    if b > ymax:
        ymax = b
    if b < ymin:
        ymin = b

print((xmax - xmin) * (ymax - ymin))