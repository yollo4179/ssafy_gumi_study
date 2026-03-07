import sys
sys.stdin = open('input.txt')

arr = [[0] * 1001 for _ in range(1001)]  # 무식하게풀기

N = int(input())
for i in range(1, N + 1):
    x, y, w, h = map(int, input().split())

    for j in range(w):
        for k in range(h) :
            arr[y+k][x+j] = i

    # 배열의 각 칸의 수는 해당 종이의 순서(1이면 첫번째)
result = []
for i in range(1, N + 1):
    cnt = 0
    for row in arr:
        for column in row:
            if column == i:
                cnt += 1
    result.append(cnt)

for i in result :
    print(i)