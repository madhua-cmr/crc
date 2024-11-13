def calculate_crc(data, divisor):
    dividend = int(data + "00000000", 2)
    divisor = int(divisor, 2)
    
    for i in range(8):
        if dividend & (1 << (15 - i)):
            dividend ^= divisor << (7 - i)
    
    remainder = bin(dividend)[-8:]
    return remainder.zfill(8)

data = input()
divisor = input()

crc = calculate_crc(data, divisor)

print(crc)
