import sys ; sys.stdin = open('input.txt')

def sol(str1, str2):
    str1 = list(set(str1)) # 중복 제거 후 리스트로 변환
    char_cnt = {}
    for i in str1:
        cnt = 0
        for j in str2:
            if j == i :
                cnt += 1
        char_cnt[i] = cnt
    max_cnt = 0
    for char in char_cnt:
        if char_cnt[char] > max_cnt:
            max_char = char
            max_cnt = char_cnt[char]
    return max_cnt

T = int(input())
for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    print(f'#{tc} {sol(str1, str2)}')
