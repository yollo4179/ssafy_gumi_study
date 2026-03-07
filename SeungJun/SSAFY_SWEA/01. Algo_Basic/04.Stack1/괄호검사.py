import sys ; sys.stdin = open('2_input.txt')


def sol(s):
    stack = [0] * 1000
    top = -1
    for c in s :
        if c in '{(':
            top += 1
            stack[top] = c
        elif c in '})':
            if top > -1:
                if c == '}' and stack[top] == '{':
                    top -= 1
                elif c == ')' and stack[top] == '(':
                    top -= 1
                else:
                    return 0
            else:
                return 0
    if top == -1:
        return 1
    else:
        return 0


T = int(input())
for tc in range(1,T+1):
    s = input()
    print(f'#{tc} {sol(s)}')