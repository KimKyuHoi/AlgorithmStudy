#n x m 크기의 금광이 있습니다. 금광은 1 x 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어 있습니다.
#채굴자는 첫 번쨰 열부터 출발하여 금을 캐기 시작합니다. 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있습니다. 이후에 m번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동해야 합니다. 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하세요.

import sys
input = sys.stdin.readline

t = int(input())
 
n, m = map(int, input().split())

array = list(map(int, input().split()))

dp = []
index = 0
for i in range(n):
    dp.append(array[index:index+m])
    index += m
for j in range(1,m):
    for i in range(n):
        if i == 0: left_up  = 0
        else: left_up = dp[i-1][j-1]
        
        if i == n-1: left_down = 0
        else: left_down = dp[i+1][j-1]
        
        left = dp[i][j-1]
        dp[i][j] = dp[i][j] + max(left_up, left_down, left)

result = 0
for i in range(n):
    result = max(result, dp[i][m-1])
print(result)   