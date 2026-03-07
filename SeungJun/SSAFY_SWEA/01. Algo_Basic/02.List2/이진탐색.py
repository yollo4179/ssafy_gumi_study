import sys ; sys.stdin = open('input.txt')

def solution(p, a, b) :
    l_a = l_b = 1
    r_a = r_b = p
    cnt_a = cnt_b = 0
    while l_a <= r_a :
        c_a = int((l_a + r_a) / 2)
        if a > c_a :
            l_a = c_a
            cnt_a += 1
        elif a < c_a :
            r_a = c_a
            cnt_a += 1
        else :
            break
    while l_b <= r_b:
        c_b = int((l_b + r_b) / 2)
        if b > c_b :
            l_b = c_b
            cnt_b += 1
        elif b < c_b :
            r_b = c_b
            cnt_b += 1
        else:
            break
    if cnt_a < cnt_b :
        return 'A'
    elif cnt_b < cnt_a :
        return 'B'
    else :
        return 0

T = int(input())
for tc in range(1, T+1):
    p, a, b = map(int, input().split())
    print(f'#{tc}', end=' ')
    print(solution(p, a, b))
