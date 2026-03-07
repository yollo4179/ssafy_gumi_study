import sys ; sys.stdin = open('input.txt')

def my_len(s):
    cnt = 0
    for _ in s:
        cnt += 1
    return cnt

def sol(s1,s2):
    s1_len = my_len(s1)  # 7
    s2_len = my_len(s2)  # 2
    cnt = 0
    not_s2_cnt = 0
    i = 0
    while i < (s1_len - s2_len + 1):  # i < 6
        if s2 == s1[i:i+s2_len]:  # i = 1, 1:3(1,2)
            cnt += 1
            i += s2_len  # i = 3이려면
        else:
            not_s2_cnt += 1
            i += 1
    return cnt + not_s2_cnt + s1_len - i

T = int(input())
for tc in range(1,T+1):
    s1, s2 = input().split()
    print(f'#{tc} {sol(s1,s2)}')