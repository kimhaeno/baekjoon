import math

while True:
    n = int(input())
    if n == -1:
        break
    div = []
    sum = 1

    for i in range(2, n//2 + 1):
        if n == i:
            break
        if n%i==0:
            div.append(i)
            sum += i
        if sum > n:
            break
    
    if sum == n:
        print(f"{n} = 1", end ="")
        for i in div:
            print(f" + {i}", end = "")
        print("")
    else:
        print(f"{n} is NOT perfect.")

