# 2차원 배열의 sum 구하기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

s = 0

for i in range(N) :
    for j in range(M) :
        s += arr[i][j]

# 2차원 배열 순회
# 열 우선 순회
# i 행의 좌표
# j 열의 좌표

for j in range(m) :
    for i in range(n) :
        function(array[i][j])

# 지그재그 순회(행 순회)
# 중요하진 않은데 그냥 이런 게 있다 정도

for i in range(n) :
    for j in range(m) :
        func(array[i][j + (m-1-2*j) * (i%2)])
        # 짝수 줄(인덱스 1, 3, 5, ..)에서는 역순으로 순회

# 델타를 이용한 2차원 탐색
arr[
