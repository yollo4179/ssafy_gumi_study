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

def find_ratios_from_binary(code): # 특정 줄에서 숫자 뽑아내기
    global result
    result = []
    binary_ratios = [
        [2,1,1],
        [2,2,1],
        [1,2,2],
        [4,1,1],
        [1,3,2],
        [2,3,1],
        [1,1,4],
        [3,1,2],
        [2,1,3],
        [1,1,2],
    ]
    now = '1'
    code = code.rstrip('0')
    i = len(code)-1
    ratios = []
    r = 0
    while i >= 0:
        if code[i] == now: # 이전 수와 같으면
            r += 1
            i -= 1
        else: # 달라지면 r 초기화 후 새로 카운트
            ratios.append(r)
            r = 0
            if now == '1':
                now = '0'
            else:
                now = '1'
        if len(ratios) == 3:
            ratios.reverse()
            ratios = [x // min(ratios) for x in ratios]
            result.append(binary_ratios.index(ratios))
            ratios = []
            while code[i] == '0':
                i -= 1
            now = '1'
    return result


def find_code_from_input(N):
    ans = 0
    code_list = []
    for i in range(N-1):
        if i == 0:
            just_before = input().strip()
            temp = input().strip()
        else:
            temp = input().strip()

        if temp == just_before:
            continue
        else:
            binary_code = hexademical_to_binary(temp)
            decoded = find_ratios_from_binary(binary_code)
            for j in range(0, len(decoded), 8):
                eight_digit_code = decoded[j:j+8]
                eight_digit_code = eight_digit_code[::-1]
                if eight_digit_code not in code_list:
                    code_list.append(eight_digit_code)
                    odd_sum = 0
                    even_sum = 0
                    for i in range(7):
                        if i % 2 == 1 :
                            even_sum += eight_digit_code[i]
                        elif i % 2 == 0:
                            odd_sum += eight_digit_code[i]
                    if (odd_sum * 3 + even_sum + eight_digit_code[-1]) % 10 == 0:
                        ans += sum(eight_digit_code)
        just_before = temp
    return ans

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print(f'#{tc} {find_code_from_input(N)}')