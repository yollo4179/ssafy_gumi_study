import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)





T = int(input())
for tc in range(1,T+1):
    V = int(input())
    tree = [0] * (V+1)
    for _ in range(V):
        temp = list(input().split())
        if len(temp) == 2: # 정점이정수임
            idx = int(temp[0])
            val = int(temp[1])
            tree[idx] = val
        else: # 정점이연산자임
            idx = int(temp[0])
            val = temp[1] # 연산자
            c_l = int(temp[2])
            c_r = int(temp[3])
