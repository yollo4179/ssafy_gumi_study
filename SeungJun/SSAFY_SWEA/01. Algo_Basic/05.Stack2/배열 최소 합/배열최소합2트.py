import sys;sys.stdin = open('배열최소합input.txt')

def perm(lv, n, curr_sum):
    global min_v

    if lv == n:
        if min_v > curr_sum:
            min_v = curr_sum # 최소합 갱신
    elif min_v < curr_sum: # 가지치기
        return
    else:
        for i in range(lv, n):
            path[lv], path[i] = path[i], path[lv]
            perm(lv+1, n, curr_sum+arr[lv][path[lv]])
            path[lv], path[i] = path[i], path[lv]

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    path = [i for i in range(n)] # 인덱스
    min_v = 10000
    perm(0, n, 0)
    print(f'#{tc} {min_v}')