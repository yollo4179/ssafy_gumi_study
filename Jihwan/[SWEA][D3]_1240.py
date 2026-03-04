mapping = {
    '0001101': '0', '0011001': '1', '0010011':'2', '0111101': '3', '0100011':'4',
    '0110001': '5', '0101111': '6', '0111011': '7', '0110111': '8', '0001011': '9',
}

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]

    code = ''
    flag = False
    for i in range(n):
        for j in range(m-1, -1, -1):
            if arr[i][j] == '1':
                code = arr[i][j-55:j+1]
                flag = True
                break
        if flag:
            break
    
    num = ''
    for k in range(0, 56, 7):
        num += mapping[code[k:k+7]]

    even = 0
    odd = []

    for x in range(8):
        if (x + 1) % 2 == 1:
            odd.append(int(num[x]))
        else:
            even += int(num[x])

    if (even + sum(odd) * 3) % 10 == 0:
        print(f'#{t}', even+sum(odd))
    else:
        print(f'#{t}', 0)