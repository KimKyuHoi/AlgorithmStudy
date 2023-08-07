#1654번
#https://www.acmicpc.net/problem/1654

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
array =[]

for i in range(n):
    array.append(int(input()))

start = 1
end = max(array)

while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
       
        total += x // mid
        
            
    if total >= k:
        start = mid + 1
    else:
        end = mid - 1
print(end)