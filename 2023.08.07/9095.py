#9095번
#https://www.acmicpc.net/problem/9095

import sys
input = sys.stdin.readline

t = int(input())


dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,11):
    dp[i]=dp[i-3]+dp[i-2]+dp[i-1]

for _ in range(t):
    m = int(input())
    print(dp[m])
