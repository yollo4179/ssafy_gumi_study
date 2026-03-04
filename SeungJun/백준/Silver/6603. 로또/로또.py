def comb(arr, n):
    result = []
    if n > len(arr):
        return result

    if n == 1:
        for i in arr:
            result.append([i])
            
    elif n > 1:
        for i in range(len(arr) - n + 1):
            for j in comb(arr[i + 1:], n - 1):
                result.append([arr[i]] + j)

    return result

while True:
    temp = list(map(int, input().split()))
    k = temp[0]
    if k == 0:
        break
    nums = temp[1::]
    for i in comb(nums, 6):
        for j in i:
            print(j, end=' ')
        print()
    print()
