import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

T = int(input())

for tc in range(1, T+1):
    N = float(input())
    result = ''
    i = 1
    while i < 13:
        if N == 0:
            break
        quotient = int(N // (2 ** -i))
        result += str(quotient)
        N = N % (2 ** -i)
        i += 1
    if N != 0:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} {result}')