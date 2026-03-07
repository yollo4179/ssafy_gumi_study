import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

# 2진수를 10진수로 변환
def binary_to_decimal(n):
    # 전달받은 문자열을 뒤에서부터 탐색
    # 이후 10진수로 변환
    decimal_num = 0
    for i in range(len(n)):
        decimal_num += (2 ** i) * int(n[-(i+1)])

    return decimal_num

T = int(input())
for tc in range(1, T+1):
    num = input()
    print(f'#{tc}', end=' ')
    for i in range(len(num)//7):
        print(binary_to_decimal(num[i*7:i*7+7]), end=' ')
    print()

