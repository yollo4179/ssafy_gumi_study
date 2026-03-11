import sys
input = sys.stdin.readline

N, K = map(int, input().split())
number = input().strip()

counts = K
stack = []
for num in number:
    while stack and counts > 0 and stack[-1] < num:
        stack.pop()
        counts -= 1
    stack.append(num)

if len(stack) > N - K:
    print(''.join(*[stack[:N-K]]))
else:
    print(''.join(*[stack]))