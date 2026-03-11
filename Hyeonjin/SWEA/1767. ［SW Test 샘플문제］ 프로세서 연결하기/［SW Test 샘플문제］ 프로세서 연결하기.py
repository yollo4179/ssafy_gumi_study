dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# d 방향으로 전선을 끝까지 연결할 수 있는지 확인
def check(r, c, d):
    nr, nc = r + dr[d], c + dc[d]
    while 0 <= nr < N and 0 <= nc < N:
        if grid[nr][nc] != 0:  # 코어나 다른 전선을 만나면 실패
            return False
        nr += dr[d]
        nc += dc[d]
    return True

# d 방향으로 전선을 깔거나 지우고 설치한 길이를 반환
def fill(r, c, d, val):
    length = 0
    nr, nc = r + dr[d], c + dc[d]
    while 0 <= nr < N and 0 <= nc < N:
        grid[nr][nc] = val
        length += 1
        nr += dr[d]
        nc += dc[d]
    return length


def dfs(idx, core_cnt, wire_len):
    global max_cores, min_length

    # 종료 조건 -> 모든 코어를 다 탐색했을 때
    if idx == len(cores):
        # 더 많은 코어, 더 적은 전선길이 갱신
        if core_cnt > max_cores:
            max_cores = core_cnt
            min_length = wire_len
        elif core_cnt == max_cores:
            min_length = min(min_length, wire_len)
        return

    r, c = cores[idx]

    for d in range(4):
        if check(r, c, d):  # 해당 방향으로 갈 수 있다면
            # 전선 깔기
            length = fill(r, c, d, 2)
            dfs(idx + 1, core_cnt + 1, wire_len + length)   # 다음 코어
            fill(r, c, d, 0)    # 원상 복구

    # 코어 연결안하면 pass
    dfs(idx + 1, core_cnt, wire_len)



TC = int(input())
for tc in range(TC):
    N = int(input())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))

    # 코어 위치
    cores = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                if i == 0 or i == N - 1 or j == 0 or j == N - 1:    # 모서리는 제외
                    continue
                cores.append((i, j))

    max_cores = 0
    min_length = 0

    dfs(0, 0, 0)
    print(f'#{tc+1} {min_length}')