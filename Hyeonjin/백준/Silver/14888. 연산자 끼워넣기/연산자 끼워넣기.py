import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
op_counts = list(map(int, input().split()))

max_result = -float('inf')
min_result = float('inf')


def backtracking(idx, current_val):
    global max_result, min_result

    # 종료 조건
    if idx == N:
        max_result = max(max_result, current_val)
        min_result = min(min_result, current_val)
        return

    # 연산자 하나씩 시도
    for i in range(4):
        if op_counts[i] > 0:  # 남은 연산자가 있을 때만 실행
            # 연산자 사용 처리
            op_counts[i] -= 1

            next_val = current_val
            if i == 0:
                next_val += numbers[idx]
            elif i == 1:
                next_val -= numbers[idx]
            elif i == 2:
                next_val *= numbers[idx]
            elif i == 3:
                next_val = int(next_val / numbers[idx])

            # 다음 숫자
            backtracking(idx + 1, next_val)

            # 원상 복구
            op_counts[i] += 1


backtracking(1, numbers[0])

print(int(max_result))
print(int(min_result))