import math

TC = int(input())

for i in range(TC):
    n = int(input())

    if n <= 2:
        print(2)
        continue

    while True:
        isPrime = True
        bound = math.ceil(math.sqrt(n)) + 1
        for i in range(2, bound):
            if n%i == 0:
                isPrime = False
                break
        if isPrime:
            print(n)
            break
        n += 1
    