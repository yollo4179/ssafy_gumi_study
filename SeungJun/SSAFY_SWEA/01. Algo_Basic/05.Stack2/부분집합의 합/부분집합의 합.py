import sys ; sys.stdin = open('부분집합의합input.txt')

def powerset(lv, curr_sum):
    global ans
    if lv == n:
        if curr_sum == 0:
            temp = []
            for i in range(n):
                if path[i] == 1:
                    temp.append(arr[i])
            subsets.append(temp)

    else :
        path[lv] = 1
        powerset(lv+1, curr_sum+arr[lv])
        path[lv] = 0
        powerset(lv+1, curr_sum)


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    path = [0] * n
    subsets = []
    powerset(0, 0)
    if subsets == [[]]:
        ans = 0
    else:
        ans = 1
    print(f'#{tc} {ans}')