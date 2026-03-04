k, n = map(int, input().split())

answer = []

def choose(num):
    if num > n:
        print(*(answer))
        return

    for i in range(1, k + 1):
        answer.append(i)
        choose(num + 1) 
        answer.pop()
choose(1)