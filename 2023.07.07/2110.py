#2110번
#https://www.acmicpc.net/problem/2110

import sys
input = sys.stdin.readline

n , c = map(int, input().split())

arrays =[int(input()) for _ in range(n)]
arrays.sort()

start = 1
end = array[-1] - array[0]

result = 0
while (start <= end):
    mid = (start + end) // 2
    count = 1
    value = array[0]
    for i in array:
        if value + mid <= i:
            count += 1
            value = i
    if count < c:
        end = mid - 1
    else:
        result = mid
        start = mid + 1  
print(result)