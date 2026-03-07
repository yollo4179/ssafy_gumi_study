# 10진수를 2진수로 변환
def decimal_to_binary(n):
    binary_num = ''

    # 0보다 클 때까지 2로 나눈다
    # 나머지를 정답에 추가한다

    while n > 0:
        remain = n % 2

        binary_num = str(remain) + binary_num
        n //= 2

    return binary_num

print(decimal_to_binary(75))

# 히든 케이스 : n이 0일때를 고려해야 함
# 상기 함수는 n=0이면 빈 스트링을 return함

def decimal_to_binary(n):
    binary_num = ''

    # 0보다 클 때까지 2로 나눈다
    # 나머지를 정답에 추가한다

    # n = 0일때 예외 케이스 추가
    if n == 0:
        return 0

    while n > 0:
        remain = n % 2

        binary_num = str(remain) + binary_num
        n //= 2

    return binary_num

print(decimal_to_binary(0))

# 10진수를 2진수로 변환
def decimal_to_hexadecimal(n):
    hexadecimal_num = ''
    hex_digits = '0123456789ABCDEF'
    # 16진수는 ABCDEF 사용을 위해 먼저 매핑해야 함
    if n == 0:
        return 0

    while n > 0:
        remain = n % 16
        hexadecimal_num = hex_digits[remain] + hexadecimal_num
        n = n //16

    return hexadecimal_num

print(decimal_to_hexadecimal(17))

# 사실 내장함수 있음,,
print(bin(25))
print(hex(17))