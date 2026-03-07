import sys ; sys.stdin = open('input.txt')

def find_palindrome(word, n, m) :
    for i in range(n-m+1):
        find_word = word[i:i+m]
        if find_word == find_word[::-1]:
            return find_word
    else:
        return False

T = int(input())
for tc in range(1,T+1):
    n, m = map(int, input().split())
    words = [list(input()) for _ in range(n)]
    for i in range(n): # 한줄씩
        ans = find_palindrome(''.join(words[i]), n, m)
        if ans:
            print(f'#{tc} {ans}')
            break
    words = list(map(list, zip(*words))) # 전치 행렬

    for i in range(n): # 한줄씩
        ans = find_palindrome(''.join(words[i]), n, m)
        if ans:
            print(f'#{tc} {ans}')
            break