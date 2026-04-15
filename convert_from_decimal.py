def convert_from_decimal(number,base):
    out_put =""
    
    if number == 0:
        return ("0")
    
    if  base < 2 or  base > 36:
        return 

    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    if number < 0:
        number *= -1
        sign ="-"
    else:
        sign =""

    while number > 0:
        remainder = number % base
        out_put = digits[remainder] + out_put
        number //= base
    
    return sign + out_put


print(convert_from_decimal(26, 16))
# "1a"

print(convert_from_decimal(10, 2))
# "1010"

print(convert_from_decimal(255, 16))
# "ff"

print(convert_from_decimal(100, 7))
# "202"

print(convert_from_decimal(-42, 2))
# "-101010"