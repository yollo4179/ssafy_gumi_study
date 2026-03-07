import sys
sys.stdin = open('input.txt')

def abs_v(n) : # 절댓값 함수 직접구현
    if n >= 0 :
        return n
    else :
        return -n

def get_abs_diff(arr, x, y, n) : # i,j 좌표의 상하좌우 절댓값 합 구하는 함수
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    result = 0
    if 1 < x < n and 1 < y < n :
        for d in range(4) :
            result += abs_v(arr[y][x] - arr[y+dy[d]][x+dx[d]])

    else :
        if x in [1, n] and y in [1, n] : #모서리
            temp = 0
            for d in range(4) :
                temp += abs_v(arr[y][x] - arr[y+dy[d]][x+dx[d]])
            temp -= 2 * arr[y][x]
            result += temp
        else : # 모서리를 제외한 테두리
            temp = 0
            for d in range(4) :
                temp += abs_v(arr[y][x] - arr[y+dy[d]][x+dx[d]])
            temp -= arr[y][x]
            result += temp
    return result

T = int(input())
for tc in range(1, T+1) :
    n = int(input())
    arr = [[0] * (n+2) for _ in range(n+2)]
    total = 0
    for _ in range(1, n+1) :
        arr[_][1:n+1] = list(map(int, input().split()))
    for i in range(1, n+1) :
        for j in range(1, n+1) :
            total += get_abs_diff(arr, i, j, n)
    print(f'#{tc} {total}')