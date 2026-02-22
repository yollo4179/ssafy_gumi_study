# 중위 탐색하는 문제임

import sys, os
if os.path.exists(_f := __file__.replace('.py', 'input.txt')): sys.stdin = open(_f)


def recur(node):
    global num
    if node > n:
        return
    recur(node * 2)
    tree[node] = num
    num += 1
    recur(node * 2 + 1)
    return
# return의 기능은 '이전으로 복귀'임을 꼭 기억하자


T = int(input())
for tc in range(1,T+1):
    n = int(input()) # 정점 갯수
    tree = [0] * (n+1) # 완전 이진 트리 -> 1차원 배열
    num = 1
    recur(1)
    print(f'#{tc} {tree[1]} {tree[n//2]}')