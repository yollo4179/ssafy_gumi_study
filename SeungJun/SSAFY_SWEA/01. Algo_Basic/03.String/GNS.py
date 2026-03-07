import sys ; sys.stdin = open('input.txt')

def solution(arr, n) :
    map1 = {
        'ZRO': 0,
        'ONE': 1,
        'TWO': 2,
        'THR': 3,
        'FOR': 4,
        'FIV': 5,
        'SIX': 6,
        'SVN': 7,
        'EGT': 8,
        'NIN': 9,
    }
    map2 = {
        0: 'ZRO',
        1: 'ONE',
        2: 'TWO',
        3: 'THR',
        4: 'FOR',
        5: 'FIV',
        6: 'SIX',
        7: 'SVN',
        8: 'EGT',
        9: 'NIN',
    }
    for i in range(n) : # 각 문자-숫자를 아라비아 숫자로 치환
        arr[i] = map1[arr[i]]
    for i in range(n-1, 0, -1) : # 버블 정렬
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    for i in range(n) :
        arr[i] = map2[arr[i]]
    for i in arr:
        print(i, end=' ')

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    nums = list(input().split())
    print(f'#{tc}', end=' ')
    solution(nums, n)
    print()