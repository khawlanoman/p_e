def convert_to_decimal(number_str,base):
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"
    number_str =number_str.lower()
    value = 0

    if number_str[0] == "-":
        sign = -1
        number_str = number_str[1:]
    else:
        sign =1

    for i in number_str:
        if i not in digits:
            return "not valid"
        digit_chr = digits.index(i)
    
        if digit_chr > base:
            return "not valid"
        value = value * base + digit_chr
    return sign * value


def convert_from_decimal(number, base):
    out_put =""
    digits = "0123456789abcdefghijklmnopqrstuvwxyz"

    if number == 0:
        return "0"
    if base <2 and base > 36:
        return "base not valid"
    if number < 0:
        sign = "-"
        number *= -1
    else:
        sign =""
    while  number > 0:
        remainder = number % base
        out_put = digits[remainder] + out_put
        number //= base
    out_put = out_put.upper()
    return sign + out_put

def convert_base(number_str,source_base,target_base):
    decimal = convert_to_decimal(number_str,source_base)
    if isinstance(decimal,str):
        return decimal
    
    return convert_from_decimal(decimal,target_base)

print(convert_base("1010", 2, 16))
# "A"
print(convert_base("17", 8, 10))
# "15"

print(convert_base("123", 7, 13))
# "51"

print(convert_base("255", 10, 2))
# "11111111"

print(convert_base("0", 2, 36))
# "0"