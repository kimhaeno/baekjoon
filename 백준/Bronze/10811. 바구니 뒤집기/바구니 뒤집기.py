n, m = map(int, input().split())

li = [i+1 for i in range(n)]

for x in range(m):
    i, j = map(int, input().split())
    for y in range(i-1, i+(j-i)//2):
        tmp = li[y]
        li[y] = li[(j-y)+i-2]
        li[(j-y)+i-2] = tmp
for i in li:
    print(i, end=" ")