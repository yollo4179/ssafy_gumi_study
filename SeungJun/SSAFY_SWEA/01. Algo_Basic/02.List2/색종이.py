import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    canvas = [[0] * 10 for _ in range(10)]
    cnt = 0
    n = int(input())
    for _ in range(n) :
        x, y, ex, ey, color = map(int, input().split())
        for i in range(x,ex+1) :
            for j in range(y, ey+1) :
                canvas[j][i] += color
    for i in range(10) :
        for j in range(10) :
            if canvas[i][j] == 3 :
                cnt += 1
    print(f'#{tc} {cnt}')