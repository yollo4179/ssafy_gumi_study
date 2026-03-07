'''
집합 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]에서 부분집합의 합이 10인 갯수를 구하시오
'''
def powerset(lv):
    global ans, cnt
    cnt += 1
    if lv == n: # 최대 깊이 도달시
        sum_v = 0
        for i in range(n):
            if path[i] == 1:
                sum_v += arr[i]
        if sum_v == 10:
            ans += 1
            for i in range(n):
                if path[i] == 1:
                    print(arr[i], end=' ')
            print()
    else:
        # 트리의 각 가지(0일때와 1일때) 분기
        # 왼쪽에 1 넣기
        path[lv] = 1
        powerset(lv+1) # 계속 재귀
        # 오른쪽에 0 넣기
        path[lv] = 0
        powerset(lv+1)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
path = [0] * n
ans = cnt = 0
powerset(0)
print(ans, cnt)