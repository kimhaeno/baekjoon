arr = []

n = int(input())
for i in range(n):
    arr.append(tuple(map(int, input().split())))

arr.sort()

dp = [0 for i in range(n)]

dp[0] = 1

for i in range(1, n):
    for j in range(i):
        if arr[i][1] > arr[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(n - max(dp))