import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1) :
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    total = 0
    for i in range(5) :
        total += arr[i][i]
        total += arr[i][-(i+1)]
    total -= arr[2][2] #중복이므로 1번 뺌

    print(f'#{tc} {total}')