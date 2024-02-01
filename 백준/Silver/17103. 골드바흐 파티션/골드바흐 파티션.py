prime = [True for i in range(1000001)]

prime[0] = False
prime[1] = False
for i in range(2, 1000001):
    if not prime[i]:
        continue
    for j in range(2*i, 1000001, i):
        prime[j] = False

TC = int(input())

for i in range(TC):
    num = int(input())
    a = b = num//2
    cnt = 0

    while a>1:
        if prime[a] and prime[b]:
            cnt += 1
        a -= 1
        b += 1
    
    print(cnt)