import sys;sys.stdin = open('배열최소합input.txt')

def f(i, N, s):
    global min_v

    if i == N:
        if min_v > s:
            min_v = s
    elif min_v < s:
        return
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i+1, N, s + arr[i][p[i]])
            p[i], p[j] = p[j], p[i]


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    p = [i for i in range(n)]
    min_v = 10000
    f(0, n, 0)
    print(f'#{tc} {min_v}')