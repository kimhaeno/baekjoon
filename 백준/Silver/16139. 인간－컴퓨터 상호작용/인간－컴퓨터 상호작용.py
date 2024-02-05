import sys


S = input()
q = int(input())

alpha = [[0 for i in range(len(S) + 1)] for j in range(26)]

for i in range(1, len(S)+1):
    for j in range(26):
        alpha[j][i] = alpha[j][i-1] + (1 if S[i-1] == chr(j + ord('a')) else 0)

for i in range(q):
    a, l, r = sys.stdin.readline().split()
    a = ord(a) - ord('a')
    l = int(l)
    r = int(r)
    print(alpha[a][r+1] - alpha[a][l])
