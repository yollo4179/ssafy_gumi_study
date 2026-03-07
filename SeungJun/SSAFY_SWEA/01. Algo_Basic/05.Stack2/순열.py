def perm(lv):
    if lv == n:
        print(arr)
    else:
        for i in range(lv, n):
            arr[i], arr[lv] = arr[lv], arr[i]
            perm(lv+1)
            arr[i], arr[lv] = arr[lv], arr[i]

arr = [1, 2, 3]
n = len(arr)
perm(0)