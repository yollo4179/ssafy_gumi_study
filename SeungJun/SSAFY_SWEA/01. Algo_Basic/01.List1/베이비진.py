import sys
sys.stdin = open('input.txt')

T = int(input())

def baby_gin(num) :
    c = [0] * 12
    for i in range(6) :
        c[num % 10] += 1
        num //= 10
    i = 0
    triplet = rn = 0
    while i < 10 :
        if c[i] >= 3 : # triplet 조사
            c[i] -= 3 # 트리플렛 있으면 3만큼 개수 제거(추출)
            triplet += 1
            continue # 다시위로
        if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1 : #run 조사
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            rn += 1
            continue # 다시위로
        i += 1
    if rn + triplet == 2 :
        return 1
    else :
        return 0

for tc in range(1, T+1) :
    n = int(input())
    print(f'#{tc} {baby_gin(n)}')