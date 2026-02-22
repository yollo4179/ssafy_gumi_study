import sys;sys.stdin = open('subtreeinput.txt')

def sol(n):
    global cnt
    cnt += 1
    if tree[n][0] != 0:
        sol(tree[n][0])
    if tree[n][1] != 0:
        sol(tree[n][1])


T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    tree = [[0] * 2 for _ in range(E+2)]
    for i in range(E):
        p, c = arr[2*i], arr[2*i+1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c
    cnt = 0
    sol(N)
    print(f'#{tc} {cnt}')
