# 백준 알고리즘 2751번
#https://www.acmicpc.net/problem/2751

import sys

n = int(input())
array=[]

for i in range(n):
    array.append(int(sys.stdin.readline()))

for i in sorted(array):
    print(i)
    
    
    
    
# 한줄평 input() 보단 sys.stdin.readline()이 상대적으로 더 빠르다.
# input() 함수의 경우 prompt message를 출력하고 개행 문자(\n)를 삭제한 값을 리턴해서 느리다고 한다.