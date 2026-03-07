import sys ; sys.stdin  = open('Forthinput.txt')

def forth(inf):
    stack = [0] * 100
    top = -1
    for token in inf:
        if token not in '+-*/.':
            top += 1
            stack[top] = int(token)
        else:
            if token == '.':
                if top == 0:
                    return stack[top]
                else:
                    return 'error'
            else :
                if top > 0:
                    pop1 = stack[top]
                    top -= 1
                    pop2 = stack[top]
                    top -= 1
                    if token == '+':
                        top += 1
                        stack[top] = pop2 + pop1
                    elif token == '-':
                        top += 1
                        stack[top] = pop2 - pop1
                    elif token == '*':
                        top += 1
                        stack[top] = pop2 * pop1
                    elif token == '/':
                        top += 1
                        stack[top] = pop2 // pop1
                else:
                    return 'error'

T = int(input())

for tc in range(1,T+1):
    inf = input().split()
    print(f'#{tc} {forth(inf)}')
