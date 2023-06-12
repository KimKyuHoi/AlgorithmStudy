#10825번
#https://www.acmicpc.net/problem/2751

import sys
input = sys.stdin.readline

n = int(input())

array = []

for i in range(n):
    array.append(list(input().split()))

array.sort(key = lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in array:
    sys.stdout.write(str(student[0] + "\n"))