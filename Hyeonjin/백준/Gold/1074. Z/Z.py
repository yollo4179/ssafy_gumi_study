
# [로직전략]
# 1. Z함수
# 1-1. 현재 크기의 절반 길이, 한 사분면의 크기 구하기
# 1-2. 목표 좌표가 어떤 사분면에 있는지 확인하기
# 1-3. pass한 사분면은 skip, 사분면의 크기 +

import sys
input = sys.stdin.readline


def find_Z(n, r, c):
    # 지도가 1x1 칸이 되면 탐색 종료
    if n == 0:
        return 0
    
    d = 2 ** (n - 1)  # 현재 지도의 절반 길이
    area = d * d      # 한 사분면의 크기
    
    # 1사분면
    if r < d and c >= d:
        return area + find_Z(n - 1, r, c - d)
    
    # 2사분면
    if r < d and c < d:
        return find_Z(n - 1, r, c)
    
    # 3사분면
    if r >= d and c < d:
        return area * 2 + find_Z(n - 1, r - d, c)

    # 4사분면
    if r >= d and c >= d:
        return area * 3 + find_Z(n - 1, r - d, c - d)


n, r, c = map(int, input().split())
print(find_Z(n, r, c))

