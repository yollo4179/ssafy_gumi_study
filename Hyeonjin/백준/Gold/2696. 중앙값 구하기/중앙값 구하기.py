
# [로직전략]
# 1. 중앙값의 개수는 (M + 1) // 2 이다.
# 2. 중앙값은 정렬을 하고 리스트의 중앙에 있는 idx의 값을 출력하면 된다.
# [출력조건] - 한 줄에 10개씩 출력

import sys
input = sys.stdin.readline

TC = int(input())
for tc in range(TC):
    M = int(input())
    arr = []
    for _ in range(M // 10 + 1):
        arr.extend(list(map(int, input().split())))

    result = [0] * ((M + 1) // 2)
    idx = 0

    for i in range(1, M+1, 2):
        array = sorted(arr[:i])
        result[idx] = array[(len(array) - 1) // 2]
        idx += 1
    print((M + 1) // 2)
    for i in range(0, len(result), 10):
        print(*result[i:i+10])


