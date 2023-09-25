def binary_to_decimal(binary):
    decimal = int(binary, 2)
    return decimal

def octal_to_hexadecimal(octal):
    decimal = int(octal, 8)
    hexadecimal = hex(decimal)
    return hexadecimal

binary_num = input("Enter a binary number: ")

decimal_num = binary_to_decimal(binary_num)

octal_num = input("Enter an octal number: ")

hexadecimal_num = octal_to_hexadecimal(octal_num)

print("Decimal equivalent of binary", binary_num, "is:", decimal_num)
print("Hexadecimal equivalent of octal", octal_num, "is:", hexadecimal_num)
