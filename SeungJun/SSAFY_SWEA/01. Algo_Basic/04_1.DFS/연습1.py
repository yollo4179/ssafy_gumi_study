import sys;sys.stdin = open('연습1_input.txt')

V, E = map(int, input().split()) # V = vertex(정점), E = edge(간선)
# 인접리스트, 방문리스트 필요
adj = [[] for _ in range(V+1)] # V+1인 이유 : 0번 인덱스는 사용하지 않음
visited = [0] * (V+1)
temp = list(map(int, input().split()))
# 인접리스트에 저장
for i in range(E):
    s, e = temp[2*i], temp[2*i+1] # 둘씩 짝지어서 체크
    adj[s].append(e)
    adj[e].append(s) # 화살표 없는 양방향
cnt = 0
def dfs(v): # v = 시작 정점
    global cnt
    # 방문체크 + 할일
    visited[v] = True
    cnt += 1
    print(v, end=' ')
    # v와 인접한 정점(w) 방문 여부 확인 - 미방문시 dfs(w)
    for w in adj[v]:
        if visited[w] != True:
            dfs(w)
dfs(1)
print()
print(cnt)