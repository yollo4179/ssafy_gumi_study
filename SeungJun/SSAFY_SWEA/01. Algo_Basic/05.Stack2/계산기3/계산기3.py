import sys ; sys.stdin  = open('계산기3input.txt')


def calc(inf):
    stack = []
    postf = ''
    icp = {
        '(': 3,
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1,
    }
    isp = {
        '(': 0,
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1,
    }

    for t in inf:
        if t not in '()+-*/':
            postf += t
        elif t == ')':
            while stack and stack[-1] != '(':
                postf += stack.pop() # ( 나올때까지 pop
            stack.pop() # ( 제거
        else:
            while stack and icp[t] <= isp[stack[-1]]:
                postf += stack.pop()
            stack.append(t) # t push

    while stack:
        postf += stack.pop()

    # 후위식 계산
    stack = [0] * 100
    top = -1
    for t in postf:
        if t not in '+-*/.':
            top += 1
            stack[top] = int(t)
        else:
            if top > 0:
                pop1 = stack[top]
                top -= 1
                pop2 = stack[top]
                top -= 1
                if t == '+':
                    top += 1
                    stack[top] = pop2 + pop1
                elif t == '-':
                    top += 1
                    stack[top] = pop2 - pop1
                elif t == '*':
                    top += 1
                    stack[top] = pop2 * pop1
                elif t == '/':
                    top += 1
                    stack[top] = pop2 / pop1
    return stack[top]


T = int(input())
for tc in range(1,T+1):
    n = int(input())
    inf = input()
    print(f'#{tc} {calc(inf)}')