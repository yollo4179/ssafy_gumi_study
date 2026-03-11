import sys
input = sys.stdin.readline

words = input().strip()
bomb = input().strip()

stack = []
for word in words:
    stack.append(word)
    if stack[-1] == bomb[-1]:
        if ''.join(stack[-len(bomb):]) == bomb:
            for _ in range(len(bomb)):
                stack.pop()
if stack:
    print(''.join(stack))
else:
    print('FRULA')