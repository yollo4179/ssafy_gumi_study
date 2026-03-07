import sys ; sys.stdin = open('종이붙이기input.txt')


def sol(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return sol(n-1) + 2 * sol(n-2)

T = int(input())
for tc in range(1,T+1):
    n = int(input()) / 10
    print(f'#{tc} {sol(n)}')