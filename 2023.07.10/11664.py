#11664번
#https://www.acmicpc.net/problem/11664

import sys
input = sys.stdin.readline

ax, ay, az, bx, by, bz, cx, cy, cz = map(int, input().split())

answer = float('inf')

while  True:
    mx,my,mz = (ax+bx)/2, (ay+by)/2, (az+bz)/2
    h1 = ((ax -cx)**2 + (ay-cy)**2 + (az-cz)**2)**0.5
    h2 = ((bx -cx)**2 + (by-cy)**2 + (bz-cz)**2)**0.5
    m = ((mx-cx)**2 + (my-cy)**2 + (mz-cz)**2)**0.5
    
    if abs(answer - m) <= 1e-6:
        print('%0.10f'%answer)
        exit()
        
    if m < answer:
        answer = m
        
    if h1 > h2:
        ax, ay, az = mx, my, mz
    
    else:
        bx, by, bz = mx, my, mz
        
