# 0과 1로 이루어진 1차 배열에서 7개씩 수를 묶어 10진수로 출력

# 2진수를 10진수로 변환
def binary_to_decimal(n):
    # 전달받은 문자열을 뒤에서부터 탐색
    # 이후 10진수로 변환
    n = str(n)
    decimal_num = 0
    for i in range(len(n)):
        decimal_num += (2 ** i) * int(n[-(i+1)])

    return decimal_num

print(binary_to_decimal(1000))

num = input().strip()

