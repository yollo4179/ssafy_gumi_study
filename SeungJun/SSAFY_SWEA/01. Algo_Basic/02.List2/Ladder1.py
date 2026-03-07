import sys ; sys.stdin = open('input.txt')

def solution(arr) :
    goal = 0
    dxs, dys = [0, 0, -1], [-1, 1, 0] # 좌-우-북 순(내려갈일 없으니 남은 제외)
    for i in range(100):
        if arr[99][i] == 2 :
            goal = i # 당첨자 칸 인덱스(열 인덱스)
            break
    x, y = 98, goal #99번째 행의 y번째 값, 이후 위로 1칸 이동
    dir = 0 # 초기값은 서

    def in_range(y):
        return 0 <= y < 100 # 해당 칸이 격자 내부인지 판단
    while x > 0:
        tx, ty = x + dxs[dir], y + dys[dir]
        if in_range(ty) and arr[tx][ty] == 1 : # 가고자 하는 칸이 격자 내부이고 값이 1이면
            if dir == 0 or dir == 1: # 그리고 그 방향이 좌 or 우라면
                arr[x][y] = 9 # 밟은 칸 탐색완료
                x, y = tx, ty # 해당 칸으로 이동
            else : # 위라면 : 좌우에도 값이 있는지 탐색
                if in_range(y + dys[0]) and arr[x + dxs[0]][y + dys[0]] == 1 : # 좌우에 1이 있다면?
                    arr[x][y] = 9
                    y -= 1
                elif in_range(y + dys[1]) and arr[x + dxs[1]][y + dys[1]] == 1 :
                    arr[x][y] = 9
                    y += 1
                else: # 좌우가 격자 밖이거나 값이 없다면
                    arr[x][y] = 9
                    x -= 1
        else : # 격자 밖이거나 값이 1이 아니면
            dir = (dir+4) % 3 # 방향 전환(0->1->2->0)
    print(y)

T = 10
for tc in range(1, T+1) :
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    print(f'#{tc}', end=' ')
    solution(arr)