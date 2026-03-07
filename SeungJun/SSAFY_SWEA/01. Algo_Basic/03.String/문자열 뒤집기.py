import sys ; sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    txt = list(input())
    temp = [0] * n
    for i in range(n) :
        temp[n-1-i], temp[i] = txt[i], txt[n-1-i]
    print(f'#{tc} {"".join(temp)}')
