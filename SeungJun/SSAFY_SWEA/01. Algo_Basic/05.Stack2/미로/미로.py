import sys ; sys.stdin  = open('미로input.txt')


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def dfs_delta(x, y):
    visited[x][y] = 1
    # 4방향 탐색 후 벽이 아니고 미방문 칸이면 해당 칸으로 이동
    for d in range(4):
        nx, ny = x + dxs[d], y + dys[d]
        if in_range(nx, ny) and visited[nx][ny] == 0 and maze[nx][ny] != 1:
            dfs_delta(nx, ny)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    maze = []
    for i in range(n):
        temp = [int(x) for x in input()]
        if 2 in temp:
            sx, sy = i, temp.index(2)
        if 3 in temp:
            ex, ey = i, temp.index(3)
        maze.append(temp)

    visited = [[0] * n for _ in range(n)]
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    dfs_delta(sx, sy)
    if visited[ex][ey] == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')