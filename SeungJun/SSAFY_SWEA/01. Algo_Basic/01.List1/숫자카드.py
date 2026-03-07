import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1) :
    n = int(input())
    nums = input()
    result = [0] * 10
    max_show_number = 0
    for i in nums :
        result[int(i)] += 1 #각 숫자 출현 빈도 리스트

    for i in range(10) :
        if result[i] >= max_show_number :
            max_show_number = result[i]
            ans = i

    print(f'#{tc} {ans} {max_show_number}')