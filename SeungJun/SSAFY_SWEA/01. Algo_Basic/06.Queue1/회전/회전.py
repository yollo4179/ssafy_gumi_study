import sys ; sys.stdin = open('회전input.txt')


def rotate(q, m):
    for i in range(m):
        temp = q.pop(0)
        q.append(temp)
    return q[0]

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    print(f'#{tc} {rotate(q, m)}')