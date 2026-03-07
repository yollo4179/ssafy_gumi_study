import sys ; sys.stdin = open('1_input.txt')


def sol(s):
    stack = [0] * 1000
    top = -1
    for c in s :
        if top != -1:
            if c == stack[top]:
                top -= 1
            else:
                top +=1
                stack[top] = c
        else :
            top += 1
            stack[top] = c
    return top+1


T = int(input())
for tc in range(1,T+1):
    s = input()
    print(f'#{tc} {sol(s)}')