from sys import stdin
def hex_to_decimal(hex, hex_len):
    res = 0
    for i in range(hex_len):
        hexa = hex[hex_len-1-i]
        chars = ['A', 'B', 'C', 'D', 'E', 'F']
        #         65   66   67  68    69   70    (-55)
        if hexa in chars: #문자일 경우, 각 문자에 대응하는 hexa 값으로 변환
            hexa = ord(hexa)-55
        else:
            hexa = int(hexa)
        res += hexa*(16**i)
    return res
hex = stdin.readline().rstrip()
print(hex_to_decimal(hex, len(hex)))






#파이썬 기능 활용
# print(int(input(), 16))