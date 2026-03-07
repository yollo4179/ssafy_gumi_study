import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

code = {
    '0001101':0,
    '0011001':1,
    '0010011':2,
    '0111101':3,
    '0100011':4,
    '0110001':5,
    '0101111':6,
    '0111011':7,
    '0110111':8,
    '0001011':9,
}

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [str(input()) for _ in range(n)]
    for row in arr:
        if '1' in row:
            arr = row
            break
    arr = arr.rstrip('0')
    arr = '0' + arr
    temp = []
    result = []
    start = len(arr) - 56
    for i in range(8):
        temp.append(arr[start+7*i:start+7*(i+1)])
    for s in temp:
        result.append(code[s])
    if (sum(result[0::2]) * 3 + sum(result[1::2])) % 10 == 0:
        ans = sum(result)
    else:
        ans = 0
    print(f'#{tc} {ans}')
