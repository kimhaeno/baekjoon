a = int(input())

b = int(input())

c = int(input())

s = str(a*b*c)

for i in range(10):
    print(s.count(chr(ord("0") + i)))

    