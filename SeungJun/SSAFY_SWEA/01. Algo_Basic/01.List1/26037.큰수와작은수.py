# 연습1
# import sys
# sys.stdin = open('연습1_input.txt')

T = int(input()) # 테스트케이스
for tc in range(1, T+1) :
    N = int(input())
    arr = list(map(int, input().split()))

    max_v = arr[0]
    min_v = arr[0]
    for i in arr :
        if i > max_v :
            max_v = i
    for i in arr :
        if i < min_v :
            min_v = i
    ans = max_v - min_v
    print(f'#{tc} {ans}')