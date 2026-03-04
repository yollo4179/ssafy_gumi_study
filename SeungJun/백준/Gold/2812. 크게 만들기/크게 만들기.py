# from itertools import combinations
n, k = map(int, input().split())
num = list(input()) #문자열로받기

stack = []
dels = k
# 결국 제일 큰 수 n-k개를 뽑아야 한다(순서는 고정한 채로)
for i in num:
    while stack and dels > 0 and stack[-1] < i:
        stack.pop() # 다음 수보다 작으면 제거
        dels -= 1 # 뺄 수 있는 수 하나 감소
    stack.append(i)

print(''.join(stack[:n-k])) # 맨 앞은 가장 큰 수일수밖에 없다