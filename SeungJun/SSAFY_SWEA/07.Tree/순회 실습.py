V = int(input())
arr = list(map(int, input().split()))

E = V - 1

c1 = [0] * (V + 1)
c2 = [0] * (V + 1)

par = [0] * (V + 1)

for i in range(len(arr)//2):
    p, c = arr[2 * i], arr[2 * i + 1]
    if c1[p] == 0:
        c1[p] = c
    else: # c2[p] == 0
        c2[p] = c
    par[c] = p
print(c1)
print(c2)