import sys
sys.stdin = open('input.txt')


def my_max(arr):  # 최댓값구하기
    max_v = 0
    for i in arr:
        if i > max_v:
            max_v = i
    return max_v


def my_sum(arr):  # 합구하기
    s = 0
    for i in arr:
        s += i
    return s


def row_sum(arr):
    sumlist = []
    for i in range(100):
        sumlist.append(my_sum(arr[i]))  # 각 행 합 리스트에 추가
    return my_max(sumlist)


def diagonal_rd_sum(arr):
    '''우하향 대각선(총합은 하나임)'''
    result = 0  # 대각선 숫자들만 담을 리스트
    for i in range(100):
        result += arr[i][i]  # arr[0][0],arr[1][1]+...+arr[99][99]
    return result


def diagonal_ld_sum(arr):
    '''좌하향 대각선(전치행렬해도 대각선은 그대로라 따로 만듦)'''
    result = 0
    for i in range(100):
        result += arr[i][99 - i]  # arr[0][0],arr[1][1]+...+arr[99][99]
    return result


for tc in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    numlist = []
    numlist.append(row_sum(arr))  # 행 합 최댓값 추가
    numlist.append(diagonal_rd_sum(arr))  # 우하향 합 추가
    numlist.append(diagonal_ld_sum(arr))  # 좌하향 합 추가
    arr = list(map(list, zip(*arr)))  # 전치 행렬(대각선으로 뒤집기)
    numlist.append(row_sum(arr))  # 전치행렬 후 행(원래 열이었음) 합 최댓값 추가
    print(f'#{T} {my_max(numlist)}')