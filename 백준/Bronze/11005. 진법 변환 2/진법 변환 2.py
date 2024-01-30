n, b = map(int, input().split())
nb = ""

while n > 0 :
    if n%b <10:
        nb = str(n%b) + nb
    else:
        nb = chr(ord('A') + n%b - 10) + nb
    n = n//b

print(nb)

