a = int(input())
coin = [25, 10, 5, 1]

for i in range(a):
    c = int(input())
    for unit in coin:
        print(c//unit, end=" ")
        c = c%unit
    print("")
