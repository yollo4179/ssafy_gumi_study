# [로직전략]
# 1. 퀸을 놓을 수 있는지 검사하는 함수 만들기 (8방향에 퀸이 없어야 한다.)
# 1-1. 행의 개수만큼 배열을 만들어서 행의 인덱스에 열의 위치를 넣는다.
# 1-2. 열 체크 row[x] == row[i] / 행 체크 abs(row[x] - row[i]) == x - i
# 2. 퀸을 놓는 함수 만들기 (백트래킹)
# 2-1. 종료조건 설정 : x = 0 부터 시작해서 n에 도달하면 종료
# 2-2. for문으로 순회하면서 row[x] = i로 두고, check가 True면 재귀실행

import sys
input = sys.stdin.readline


# 퀸을 놓을 수 있는지 검사하는 함수
def check(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

# 퀸을 놓는 함수
def n_queens(x):
    global counts


    # 종료조건
    if x == n:
        counts += 1
        return
    
    for i in range(n):
        row[x] = i
        if check(x):
            n_queens(x + 1)

n = int(input())

row = [0] * n
counts = 0
n_queens(0)
print(counts)

