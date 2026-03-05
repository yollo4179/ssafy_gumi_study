import sys
input = sys.stdin.readline
from collections import deque

def bfs(sr, sc):
    visited = [[0] * M for _ in range(N)]
    q = deque([(sr, sc)])
    visited[sr][sc] = 1

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    while q:
        r, c = q.popleft()

        if r == N - 1 and c == M - 1:
            return visited[r][c] #True

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                if maze[nr][nc] == 1 and visited[nr][nc] == 0:
                    visited[nr][nc] = visited[r][c] + 1 #True
                    q.append((nr, nc))

    return False

N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, input().rstrip())))

sr, sc = 0, 0

print(bfs(sr, sc))