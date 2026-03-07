import sys ; sys.stdin = open('input.txt')

def solution(arr, n) :
    for i in range(n-1) :
        max_i = i
        min_i = i
        if i % 2 == 0: # 홀수번째 칸(최댓값들)
            for j in range(i+1, n) :
                if arr[j] > arr[max_i] :
                    max_i = j
            arr[i], arr[max_i] = arr[max_i], arr[i] #최댓값과 위치 교환
        else : # 짝수번째(최솟값들)
            for j in range(i+1, n) :
                if arr[j] < arr[min_i] :
                    min_i = j
            arr[i], arr[min_i] = arr[min_i], arr[i] #최솟값과 위치 교환

    for i in range(10) :
        print(arr[i], end=' ')
    print()

T = int(input())
for tc in range(1, T+1) :
    n = int(input())
    arr = list(map(int,input().split()))
    print(f'#{tc}', end=' ')
    solution(arr,n)