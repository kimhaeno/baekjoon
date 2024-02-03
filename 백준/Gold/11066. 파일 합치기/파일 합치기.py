dp = []
sums = []
file = []

def cost(l, r):
    if l == r:
        return 0
    if dp[l][r] != 0:
        return dp[l][r]
    if l+1 == r:
        return file[l-1] + file[r-1]

    cost_min = 10**9
    
    # l~mid, mid+1~r
    for mid in range(l,r):
        cost_temp = cost(l, mid) + cost(mid+1, r) + (sums[mid] - sums[l-1]) + (sums[r] - sums[mid])
        if cost_temp < cost_min:
            cost_min = cost_temp
    
    dp[l][r] = cost_min

    return cost_min

TC = int(input())

for case in range(TC):
    n =  int(input())

    dp = [[0 for i in range(n+1)] for j in range(n+1)]

    file = list(map(int, input().split()))

    sums = [0 for i in range(n+1)]
    for i in range(n):
        sums[i+1] = file[i] + sums[i]

    print(cost(1, n))

