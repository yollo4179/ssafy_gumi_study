import sys ; sys.stdin = open('길찾기input.txt')


def dfs(v):
    # 방문체크
    visit[v] = 1
    # 다음노드
    for w in adj[v]:
        dfs(w)

T = int(input())
for tc in range(1, T+1):
    E = int(input())
    edges = list(map(int, input().split()))
    adj = [[] for _ in range(101)]
    visit = [0] * 101
    for i in range(E):
        s, e = edges[2 * i], edges[2 * i + 1]
        adj[s].append(e)
    dfs(0)
    if visit[99] == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')