import sys ; sys.stdin = open('input.txt')

def find_palindrome(word, n, m) :
    cnt = 0
    for i in range(n-m+1):
        find_word = word[i:i+m]
        if find_word == find_word[::-1]:
            cnt += 1
    return cnt

T = 10
for tc in range(1,T+1):
    n = 8
    m = int(input())
    ans = 0
    words = [list(input()) for _ in range(n)]
    for i in range(n): # 한줄씩
        ans += find_palindrome(''.join(words[i]), n, m)

    words = list(map(list, zip(*words))) # 전치 행렬

    for i in range(n): # 한줄씩
        ans += find_palindrome(''.join(words[i]), n, m)
    print(f'#{tc} {ans}')