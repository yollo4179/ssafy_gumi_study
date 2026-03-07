import sys
sys.stdin = open('input.txt')

def find_max_index(heights) : # 같은 값이 여러 개일 경우 가장 왼쪽의 값을 최대로 하는 max함수 작성
    max_v = 0
    for i in range(100) :
        if heights[i] > max_v :
            max_v = heights[i]
            max_index = i
    return max_index
def find_min_index(heights) : # min함수도 작성
    min_v = 100 # 최대 상자 높이
    for i in range(100) :
        if heights[i] < min_v :
            min_v = heights[i]
            min_index = i
    return min_index

for tc in range(1, 11) :
    dumps = int(input())
    heights_list = list(map(int, input().split()))
    # heights_index = [0] * 100
    for i in range(dumps) :
        heights_list[find_max_index(heights_list)] -= 1
        heights_list[find_min_index(heights_list)] += 1

    print(f'#{tc} {heights_list[find_max_index(heights_list)] - heights_list[find_min_index(heights_list)]}')
