import sys ; sys.stdin = open('input.txt')

def my_len(w): # len함수작성
    cnt = 0
    for i in w :
        cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1) :
    str1 = input()
    str2 = input()
    ans = 0
    for i in range(len(str2)-len(str1)+1): # 4자, 10자면 10-6+1=7회 반복
        if str1 == str2[i:i+len(str1)]:
            ans = 1
    print(f'#{tc} {ans}')