import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    arr = list(map(int,input().split()))
    result = []
    for i in range(n) :
        cnt = 0
        for j in range(i+1, n) :
            if arr[i] > arr[j] :
                cnt += 1
            result.append(cnt)
    max_v = result[0]
    for i in result :
        if i > max_v :
            max_v = i
    print(f'#{tc} {max_v}')