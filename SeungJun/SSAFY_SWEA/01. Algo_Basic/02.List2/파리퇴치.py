import sys
sys.stdin = open('input.txt')

def my_max(arr) :
    max_v = 0
    for i in arr :
        if i > max_v:
            max_v = i
    return  max_v

def kill_flies(arr, n, m):
    kill_list = []
    # (n - m + 1) ** 2 번 수행, 5, 3이면 5 - 3 + 1 = 3번 수행(0~2까지)
    for y in range(n-m+1) : # 0부터 n-m까지
        for x in range(n-m+1) :
            flies = 0
            for i in range(m):
                for j in range(m):
                    flies += arr[y+i][x+j]
            kill_list.append(flies)
    return my_max(kill_list)

T = int(input())
for tc in range(1, T+1) :
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    print(f'#{tc} {kill_flies(arr, n, m)}')