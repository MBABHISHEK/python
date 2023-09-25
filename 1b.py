try:
num = input("Enter a number: ")
if not num.isdigit():
raise ValueError("Invalid input! Please enter a valid number.")
reverse_num = num[::-1]
if num == reverse_num:
print(num, "is a palindrome")
else:
print(num, "is not a palindrome")
digit_count = {}
for digit in num:
if digit in digit_count:
digit_count[digit] += 1
else:
digit_count[digit] = 1
print("Digit counts:")
for digit, count in digit_count.items():
print(digit, ":", count)
except ValueError as e:
