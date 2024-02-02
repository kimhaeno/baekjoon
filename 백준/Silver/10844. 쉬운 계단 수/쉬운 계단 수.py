dp = [[0 for i in range(10)] for j in range(100)]

n = int(input())

for i in range(1,10):
    dp[0][i] = 1

for i in range(1, n):
    for j in range(10):
        if j-1 >= 0:
            dp[i][j] += dp[i-1][j-1]
        if j+1 <= 9:
            dp[i][j] += dp[i-1][j+1]
        dp[i][j] %= 1000000000

sum = 0        
for i in range(10):
    sum += dp[n-1][i]
print(sum % 1000000000)