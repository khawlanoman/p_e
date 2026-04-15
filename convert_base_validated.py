def convert_to_decimal(number_str,base):
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    if base < 2 or  base > 36:
        return "error: invalid base"
    number_str = number_str.lower()
    value = 0
    if number_str[0] == "-":
        sign = -1
        number_str = number_str[1:]
    else:
        sign = 1
    value = 0
    for i in number_str:
        if i not in digits:
            return "not valid"
        digit_ch = digits.index(i)
        if digit_ch >= base:
            return "error: invalid digit for base"
        value = value * base + digit_ch
    return sign * value

def  convert_from_decimal(number, base):
    if number == 0:
        return "0"
    if base <2 or base > 36:
        return "error: invalid base"
    out_put = ""
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    if number < 0:
        sign = "-"
        number *= -1
    else:
        sign =""
    
    while number > 0:
        r = number % base
        out_put = digits[r] + out_put
        number //= base

    out_put = out_put.lower()
    return sign + out_put

def convert_base_validated(number_str,source_base,target_base):
    decimal = convert_to_decimal(number_str, source_base)

    if isinstance(decimal, str):
        return decimal
    
    return convert_from_decimal(decimal,target_base)


# Mixed case hex to decimal
print(convert_base_validated("Ff", 16, 10))
# "255"

# Leading zeros in hex to binary
print(convert_base_validated("00FF", 16, 2))
# "11111111"

# Base 36 (letters up to 'z') to decimal
print(convert_base_validated("z", 36, 10))
# "35"

# All zeros should become just "0"
print(convert_base_validated("0000", 7, 10))
# "0"

# Binary with leading zeros
print(convert_base_validated("0001", 2, 10))
# "1"

# Binary to hex (note: letters should be lowercase)
print(convert_base_validated("1010", 2, 16))
# "a"