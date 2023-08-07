#15990.py
#https://www.acmicpc.net/problem/15990

# import sys
# input = sys.stdin.readline

# n = int(input())

# dp = [0] * (n+1)

# dp[1] = 1
# dp[2] = 1
# dp[3] = 3
# dp[4] = 3
# dp[5] = 6
# dp[6] = 
# 1 2 1 2
# 2 1 2 1
# 123
# 132
# 321
# 312
# 213
# 231

# for i in range(4, n+1):
#     dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
# for _ in range(n):
#     m = int(input())
#     print(dp[m] % 1000000009)