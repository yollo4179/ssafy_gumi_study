import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)


def recur(node):
    if node > N - M:  # 리프 노드 반환 배제
        return
    recur(node * 2)
    recur(node * 2 + 1)
    if node * 2 + 1 <= N:
        tree[node] += tree[node * 2] + tree[node * 2 + 1]
    else:
        tree[node] += tree[node * 2]


T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    q = [0]
    for _ in range(M):
        node, num = map(int, input().split())
        tree[node] = num
    recur(1)
    print(f'#{tc} {tree[L]}')