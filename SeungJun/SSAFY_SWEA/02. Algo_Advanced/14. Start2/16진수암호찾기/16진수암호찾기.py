import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

pattern = [
    '001101',
    '010011',
    '111011',
    '110001',
    '100011',
    '110111',
    '001011',
    '111101',
    '011001',
    '101111',
]

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

def find_pattern(n):
    result = []
    i = 0
    while i <= len(n)-6:
        code = n[i:i+6]
        if code in pattern:
            result.append(pattern.index(n[i:i+6]))
            i += 5
        i += 1
    return result

T = int(input())
for tc in range(1, T+1):
    pwd = input()
    binary_num = hexademical_to_binary(pwd)
    print(f'#{tc}', end=' ')
    print(*find_pattern(binary_num))
