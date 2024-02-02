# visit = [False for i in range(9)]
curr = [0 for i in range(9)]

def back(n, m, idx):
    if idx == m:
        for i in range(1, m+1):
            print(curr[i], end=" ")
        print("")
        return
    
    for i in range(1, n+1):
        curr[idx + 1] = i
        back(n, m, idx + 1)
    




n, m = map(int, input().split())

back(n, m, 0)
