import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

def hexademical_to_binary(n):
    mapping = {
        '0':'0000',
        '1':'0001',
        '2':'0010',
        '3':'0011',
        '4':'0100',
        '5':'0101',
        '6':'0110',
        '7':'0111',
        '8':'1000',
        '9':'1001',
        'A':'1010',
        'B':'1011',
        'C':'1100',
        'D':'1101',
        'E':'1110',
        'F':'1111',
    }
    binary_num = ''
    for s in n:
        binary_num += mapping[s]

    return binary_num

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
    binary_num = hexademical_to_binary(num)
    print(f'#{tc}', end=' ')
    for i in range(len(binary_num)//7):
        print(binary_to_decimal(binary_num[i*7:i*7+7]), end=' ')
    remain = len(binary_num) % 7
    print(binary_to_decimal(binary_num[-1 * remain:]))