import sys
sys.stdin = open('input.txt')

def solution(n, m, a, b) :
    cnt = 0
    ind = 0
    for i in range(m) :
        for j in a :
            ind += 1
            if b[i] == j :
                cnt += 1
                a = a[ind:n+1]
                ind = 0
                break

    if cnt == m :
        return 'YES'
    else :
        return 'NO'
T = int(input())
for tc in range(1, T+1) :
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(f'#{tc} {solution(n, m, a, b)}')