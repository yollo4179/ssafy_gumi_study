import sys ; sys.stdin = open('피자input.txt')

def sol(arr):
    global n, m
    # 화덕에 n개 피자
    q = []
    for i in range(n):
        q.append(i) # arr[i]
    idx = n # 마지막피자
    while len(q) != 1:
        pizza = q.pop(0)
        arr[pizza] //= 2
        # 치즈 남으면 다시넣기
        if arr[pizza] != 0:
            q.append(pizza) #넣음
        # 다녹으면 다음피자 넣기
        elif idx < m:
            q.append(idx)
            idx += 1
    return q.pop() + 1


T = int(input())
for tc in range(1,T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{tc} {sol(arr)}')