#10814번
# https://www.acmicpc.net/problem/11650

import sys
input = sys.stdin.readlines

n = int(input())
array = []

for i in range(n):
    array.append(list(input().split()))
    
array.sort(key = lambda x: int(x[0]));

for i in range(n):
    print(array[i][0], array[i][1])