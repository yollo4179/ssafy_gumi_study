n, m = map(int, input().split())

print('0 1')
current_leaf = 0

for i in range(1, n - 1):
    # m이 2일 때는 일직선
    if m == 2:
        print(f"{i} {i + 1}")

    # m이 2보다 클 때
    else:
        if current_leaf < m - 1:
            print(f"1 {i + 1}")
            current_leaf += 1
        else:
            # 리프 개수가 2개를 제외하고 채워지면 그 다음부터는 일직선
            print(f"{i} {i + 1}")