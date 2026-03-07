import sys
sys.stdin = open('input.txt')

# 원소는 10개므로 가능한 부분집합의 수는 2^10 = 1024개
# 리스트 1024개 이거됨??

def is_sub_sum_0(arr, n):
    result = []  # 부분집합 목록 생성
    for i in range(1 << n):  # 부분집합 생성
        subsets = []
        for j in range(n):
            if i & (1 << j):
                subsets.append(arr[j])
        result.append(subsets)

    is_0_exist = []  # 각 부분집합의 총합 리스트
    for s in result:
        if s == []:  # 공집합 예외처리
            total = 1
        else:
            total = 0  # 각 부분집합의 총합 (sum 미사용 구현)
            for i in s:
                total += i
        is_0_exist.append(total)

    if 0 in is_0_exist:
        return 1
    else:
        return 0


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {is_sub_sum_0(arr, n)}')