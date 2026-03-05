while True:
    w, h = map(int, input().split())
    grid = []
    for _ in range(h):
        grid.append(list(map(int, input().split())))
    if w == 0 and h == 0:
        break

    counts = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1: # 땅 발견
                counts += 1
                grid[i][j] = 0
                stack = [[i, j]]

                while stack:
                    curr_i, curr_j = stack.pop()
                    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0),
                                   (1, 1), (1, -1), (-1, -1), (-1, 1)]:
                        ni, nj = curr_i + di, curr_j + dj

                        if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] == 1:
                            grid[ni][nj] = 0
                            stack.append([ni, nj])

    print(counts)