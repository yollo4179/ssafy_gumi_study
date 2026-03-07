import sys ; sys.stdin = open('3_input.txt')

row = []
def sol(n):
    global row
    if n == 1:
        row = [1]
        print(1)
    else:
        sol(n-1)  # 재귀
        temp = [1]  #맨 앞 항 계수 설정(1)
        for i in range(n-2):  # n-1에서의 row 각 항 더하기
            temp.append(row[i] + row[i+1])
        temp.append(1)  # 마지막 항 계수 추가
        row = temp
        print(*row)

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    print(f'#{tc}')
    sol(n)