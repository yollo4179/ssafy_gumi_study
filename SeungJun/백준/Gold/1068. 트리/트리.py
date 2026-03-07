n = int(input())
tree = [[] for _ in range(n)]
par = [0] * n
nums = list(map(int, input().split()))
for i in range(n):
    p = nums[i]
    if p == -1:
        root = i
    else:
        tree[p].append(i) # p번 노드의 자식에 i 추가

rm = int(input())
cnt = 0
def dfs(v):
    global cnt
    if v == rm:
        return

    is_leaf = True
    for w in tree[v]:
        if w != rm:
            is_leaf = False
            dfs(w)
    
    if is_leaf:
        cnt += 1

if rm == root :
    print(0)
else:
    dfs(root)
    print(cnt)