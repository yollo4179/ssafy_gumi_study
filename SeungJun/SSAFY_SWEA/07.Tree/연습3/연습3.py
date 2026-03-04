import sys;sys.stdin=open('input.txt')


def preorder(node):
    global cnt
    if node != 0:
        print(node, end=' ')
        preorder(tree[node][0])
        preorder(tree[node][1])
        cnt += 1


V = int(input())
E = V - 1
temp = list(map(int, input().split()))
tree = [[0] * 3 for _ in range(V+1)] # 인접리스트 [왼쪽, 오른쪽, 루트]
for i in range(E):
    p, c = temp[2 * i], temp[2 * i + 1]
    if tree[p][0] == 0 : # 왼쪽트리가 없으면
        tree[p][0] = c
    else:
        tree[p][1] = c
    tree[c][2] = p

print(tree)

# root 찾기
c = V
while tree[c][2] != 0:
    c = tree[c][2]
print(c)

cnt = 0
preorder(3)
print()
print(cnt)