import sys ; sys.stdin = open('토너먼트카드게임input.txt')


def tournament(s, e):  # 재귀
    if s == e:
        return s
    else:
        m = (s+e) // 2
        l = tournament(s, m)
        r = tournament(m+1, e)
        return rcp(l,r)


def rcp(s1, s2):
    if arr[s1] == arr[s2]:
        return s1
    else:
        if arr[s1] == 1:
            if arr[s2] == 2:
                return s2
            else:
                return s1
        elif arr[s1] == 2:
            if arr[s2] == 1:
                return s1
            else:
                return s2
        elif arr[s1] == 3:
            if arr[s2] == 2:
                return s1
            else:
                return s2

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {tournament(0,n-1)+1}')
