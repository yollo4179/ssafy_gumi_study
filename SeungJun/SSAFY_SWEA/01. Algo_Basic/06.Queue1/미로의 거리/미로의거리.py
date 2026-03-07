import sys ; sys.stdin = open('미로의거리input.txt')

drs, dcs = [-1, 0, 1, 0], [0, 1, 0, -1]
def in_range(x, y):
    global n
    return 0 <= x < n and 0 <= y < n

def start_p()
def bfs(r, c):
    q = [(r, c)]
    visited[r][c] = 1

    while q:
        r, c = q.pop(0)
        if arr[r][c] == 3:
            return visited[r][c] - 2 # 출발지 칸수 제외

    for i in range(4):
        nr, nc = r + drs[i], c + dcs[i]


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]