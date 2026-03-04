import sys, os
if os.path.exists(_f := __file__.replace('.py', '_input.txt')): sys.stdin = open(_f)

def enq(n):
    global last
    last += 1
    heap[last] = n # 마지막 정점에 값 추가

    c_node = last
    p_node = c_node // 2 # p_node가 0이면 루트노드
    while p_node and heap[p_node] > heap[c_node] : # 부모 노드가 더 크면
        heap[p_node], heap[c_node] = heap[c_node], heap[p_node] # 교환
        c_node = p_node
        p_node //= 2 # 노드 인덱스 교환

def anc_sum(n):
    node = n
    total = 0
    while node:
        node //= 2
        total += heap[node]
    return total

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = [0] * (N+1)
    last = 0
    for i in arr:
        enq(i)
    print(f'#{tc} {anc_sum(N)}')