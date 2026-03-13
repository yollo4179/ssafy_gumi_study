# 12100
# [로직전략]
# 블록 랜덤추가는 없다.
# 1-1. 0 제거하고 숫자만 남기기
# 1-2. 리스트를 순회하며 인접한 두 숫자가 같으면 하나로 합치고, 이미 합쳐진 자리는 건너뛰기
# 1-3. 합치고 남는 빈자리는 다시 0으로 채우기
# 2-1. rotate로 보드 90도 돌리기 (왼쪽으로 밀기만 실행하기)
# 2-2. rotate -> 인덱스 접근할 것 for i in range(4)
# 3-1. 메인로직 재귀함수 - 90도 돌리고 push_left했을 때 인접하는 수가 있을 때만 재귀실행, depth + 1
# 3-2. 없으면 변화가 없으니까 90도 더 돌림
# 3-3. 문제조건 depth == 5이면 재귀종료

import sys
input = sys.stdin.readline


# 1. 한 줄을 왼쪽으로 미는 함수
def push_left(row):
    # 0을 제외한 숫자만 추출
    new_row = [i for i in row if i != 0]    # 0을 제외하고 숫자만 남기기
    result = []

    skip = False
    for i in range(len(new_row)):
        if skip:
            skip = False
            continue
        # 다음 숫자와 같으면 합침
        if i + 1 < len(new_row) and new_row[i] == new_row[i + 1]:
            result.append(new_row[i] * 2)   # 같은 수면 * 2
            skip = True
        else:
            result.append(new_row[i])   # 다르면 쌓기

    # 남은 자리를 0으로 채움
    return result + [0] * (n - len(result))


# 2. 보드를 90도 회전시키는 함수
def rotate_board(board):
    new_board = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            # 좌표 변환 공식 적용
            new_board[j][n - 1 - i] = board[i][j]
    
    # return [list(row) for row in zip(*matrix[::-1])] -> 이걸로 써도 됨 (오늘 알았음)
    return new_board


# 3. 메인로직
ans = 0
def solve(depth, board):
    global ans
    # 현재 보드에서 최대값 갱신
    current_max = max(max(row) for row in board)
    ans = max(ans, current_max)

    # 문제조건 : 최대 5번 이동
    if depth == 5:
        return

    for _ in range(4):
        # 보드 회전
        board = rotate_board(board)

        # 각 행을 왼쪽으로 밀기
        moved_board = [push_left(board[i]) for i in range(n)]

        # 변화가 있는 경우에만 다음 재귀 진행 (가지치기)
        if moved_board != board:
            solve(depth + 1, moved_board)

        # 인접한 같은 수가 없으면 90도 더 돌림


# 실행부
n = int(input())
init_board = [list(map(int, input().split())) for _ in range(n)]
solve(0, init_board)
print(ans)