E, N = map(int, input().split()) # 간선 수 e, 노드 n이 루트 노드
arr = list(map(int, input().split()))

V = E + 1 # V = 마지막 정점 번호
# 자식 c1, c2 배열 생성 : 부모 번호를 인덱스로 가짐
c1 = [0] * (V + 1)
c2 = [0] * (V + 1)
for i in range(len(arr)//2):
    p, c = arr[2 * i], arr[2 * i + 1]
    if c1[p] == 0:
        c1[p] = c
    else: # c2[p] == 0
        c2[p] = c
print(c1)
print(c2)