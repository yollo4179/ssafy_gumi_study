def powerset(lv):
    if lv == n: # 최대 깊이 도달시
        for i in range(n):
            if path[i] == 1:
                print(arr[i], end = ' ')
        print()
    else:
        # 트리의 각 가지(0일때와 1일때) 분기
        # 왼쪽에 1 넣기
        path[lv] = 1
        powerset(lv+1) # 계속 재귀
        # 오른쪽에 0 넣기
        path[lv] = 0
        powerset(lv+1)

arr = [1, 2, 3]
n = len(arr)
path = [0] * n
powerset(0)