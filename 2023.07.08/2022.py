#2022번
#https://www.acmicpc.net/problem/2022

import sys
input = sys.stdin.readline

def f(x,y,w):
    h1 = (x**2 - w**2)**0.5
    h2 = (y**2 - w**2)**0.5
    c = (h1*h2)/(h1+h2)
    return c

x, y, c = map(float, input().split())
start, end = 0, min(x,y)
answer = 0
while(end-start > 0.000001):
    mid = (start + end) / 2
    if f(x,y,mid) >= c:
        answer = mid
        start = mid
    else:
        end = mid
        
print("%.3f" %answer)