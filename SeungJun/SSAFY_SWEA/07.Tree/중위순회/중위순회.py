# 완전 이진 트리는 1차원 배열로 저장하는게 유리
import sys;sys.stdin = open('중위순회input.txt')


def in_order(v):
    global ans
    if v > N:
        return
    in_order(2*v)
    ans.append(tree[v])
    in_order(2*v+1)


T = 10
for tc in range(1,T+1):
    N = int(input())
    tree = [''] * (N+1) # 문자열 빈칸 리스트
    for _ in range(N):
        txt = input().split()
        idx = int(txt[0])
        tree[idx] = txt[1]
        # txt[2::], 하위 트리

    ans = []
    in_order(1)
    print(f'#{tc}', ''.join(ans))