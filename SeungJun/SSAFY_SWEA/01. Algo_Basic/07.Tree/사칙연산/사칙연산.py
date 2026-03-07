import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

def postorder(v):
    if v > V or type(tree[v]) is not str: # 정점을 벗어나거나 해당 정점이 숫자일 경우
        return # 상위 노드(연산자)로 이동
    postorder(child_idx[v][0])
    postorder(child_idx[v][1])
    #할일
    tree[v] = calc(tree[child_idx[v][0]], tree[child_idx[v][1]], tree[v])

def calc(cl, cr, opr):
    if opr == '+':
        return cl + cr
    elif opr == '-':
        return cl - cr
    elif opr == '*':
        return cl * cr
    elif opr == '/':
        return cl / cr

T = int(input())
for tc in range(1,T+1):
    V = int(input())
    tree = [0] * (V+1)
    child_idx = [[0,0] for _ in range(V+1)]
    for _ in range(V):
        temp = list(input().split())
        if len(temp) == 2: # 정점이정수임
            idx = int(temp[0])
            val = int(temp[1])
            tree[idx] = val
        else: # 정점이연산자임
            idx = int(temp[0])
            val = temp[1] # 연산자
            c_l_idx = int(temp[2])
            c_r_idx = int(temp[3])
            tree[idx] = val
            child_idx[idx][0] = c_l_idx
            child_idx[idx][1] = c_r_idx

    postorder(1)
    print(f'#{tc} {int(tree[1])}')
