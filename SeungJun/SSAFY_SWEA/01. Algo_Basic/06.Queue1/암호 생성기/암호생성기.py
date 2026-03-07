import sys ; sys.stdin = open('암호생성기input.txt')

T = int(input())
for _ in range(T):
    tc = int(input())
    n = list(map(int, input().split()))
    i = 1
    while True:
        x = n.pop(0)
        x -= i
        if x <= 0:
            x = 0
            n.append(x)
            break
        else:
            n.append(x)
        i += 1
        if i > 5 :
            i = 1

    print(f'#{tc}', end=' ')
    print(*n)