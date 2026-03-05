import sys
input = sys.stdin.readline

N = int(input())

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

max_height = 0
for i in range(N):
    if max_height < max(grid[i]):
        max_height = max(grid[i])

safety = []
for h in range(max_height):

    counts = 0
    visited = [[False] * N for _ in range(N)]   # visited 2차원 배열 생성
    for i in range(N):
        for j in range(N):
            if grid[i][j] > h and not visited[i][j]:    # 높이보다 높고 방문하지 않은 곳이면
                counts += 1                             # 구역 1개 추가

                stack = [[i, j]]        # 현재 위치 stack append
                visited[i][j] = True    # 현재 위치 방문처리
                while stack:
                    curr_i, curr_j = stack.pop()

                    for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:   # 탐색 시작
                        ni, nj = curr_i + di, curr_j + dj

                        if 0 <= ni < N and 0 <= nj < N:                     # 이동하고자 하는 곳이 범위 안이고
                            if grid[ni][nj] > h and not visited[ni][nj]:    # h보다 높고 방문하지 않은 곳이라면
                                visited[ni][nj] = True                      # 현재 위치 방문처리
                                stack.append([ni, nj])                      # 현재 위치 stack append
    safety.append(counts)

print(max(safety))