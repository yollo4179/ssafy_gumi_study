ratio = {
    (2,1,1): '0', (2,2,1): '1', (1,2,2):'2', (4,1,1): '3', (1,3,2):'4',
    (2,3,1): '5', (1,1,4): '6', (3,1,2):'7', (2,1,3): '8', (1,1,2): '9',
}

mapping = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110',
    '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 
    'E': '1110', 'F': '1111', 
}

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    arr = [input().strip() for _ in range(n)]

    ret = 0
    duplicate = set() # 바로 전 row와 현재 row랑만 비교해서 중복 제거를 했었는데 나왔던게 나중에 다시 나올수도 있음.  

    for r in range(n):
        if r > 0 and arr[r] == arr[r-1]:
            continue
        row = ''

        for c in range(m):
            row += mapping[arr[r][c]]

        row = row.rstrip('0')
        
        if not row:
            continue
        
        
        idx = len(row)-1
        while idx >= 0:
            if row[idx] == '0':
                idx -= 1
                continue

            code = ''

            for _ in range(8):
        
                r1, r2, r3, r4 = 0, 0, 0, 0
                while row[idx] == '1':
                    r4 += 1
                    idx -= 1
                while row[idx] == '0':
                    r3 += 1
                    idx -= 1
                while row[idx] == '1':
                    r2 += 1
                    idx -= 1
                while row[idx] == '0':
                    r1 += 1
                    idx -= 1
            
                d = min(r2, r3, r4)
                if d == 0:
                    rat = (r2, r3, r4)
                    
                else:
                    rat = (r2//d, r3//d, r4//d)

                code = code + ratio[rat]

            code = code[::-1]
            if len(code) != 8:
                continue
            if code in duplicate:
                continue
            duplicate.add(code)

            even = 0
            odd = []
        
            for x in range(8):
                if (x + 1) % 2 == 1:
                    odd.append(int(code[x]))
                else:
                    even += int(code[x])

            if (even + sum(odd) * 3) % 10 == 0:
                ret += sum(odd) + even
            
            while idx >= 0 and row[idx] == '0':
                idx -= 1

    print(f'#{t}', ret)