arr = [1, 5, 5, 7]
# arr의 부분집합?

# 부분 집합의 수
print(f'arr의 부분집합의 수 : {1<<len(arr)}')

# 부분집합 모두 구하기(공집합 포함)
for i in range(1 << len(arr)):
    print(f'{i}번째 부분집합:', end=' ')

    for idx in range(len(arr)):
        if i & (1 << idx):
            # i = 부분집합 번호
            # i를 비트로 변환하여 and 여부 확인
            print(arr[idx], end=' ')
    print()