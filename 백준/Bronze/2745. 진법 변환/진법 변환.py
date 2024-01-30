n, bstr = input().split()
b = int(bstr)
sum = 0

for i in range(len(n)):
    a = 0
    if ord(n[-1-i]) >= ord('A'):
        a = ord(n[-1-i]) - ord('A') + 10
    else:
        a = int(n[-1-i])
    sum += a*(b**i)

print(sum)
    
