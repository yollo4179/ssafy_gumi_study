def is_palindrome(word):
    if word == word[::-1]:
        return 1
    else:
        return 0
T = int(input())
for tc in range(1,T+1):
    word = input()
    print(f'#{tc} {is_palindrome(word)}')