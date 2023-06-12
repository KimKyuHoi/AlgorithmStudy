#1377번
#https://www.acmicpc.net/problem/2751
import sys
input = sys.stdin.readline

n = int(input())
a = []

for i in range(n):
    a.append((int(input()), i))
    
sorted_arr = sorted(a)
answer = 0

for i in range(n):
    answer= max(answer, sorted_arr[i][1]- i + 1)

print(answer)