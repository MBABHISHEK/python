class PalindromeChecker:
    def __init__(self, value):
        self.value = value
    def is_palindrome(self):
        pass

class StringPalindrome(PalindromeChecker):
    def is_palindrome(self):
        cleaned_str = "".join(self.value.split()).lower()
        return cleaned_str == cleaned_str[::-1]

class IntegerPalindrome(PalindromeChecker):
    def is_palindrome(self):
        int_str = str(self.value)
        return int_str == int_str[::-1]

def check_palindrome(obj):
    if obj.is_palindrome():
        return f"{obj.value} is a palindrome."
    else:
        return f"{obj.value} is not a palindrome."

input_value = input("Enter a string or integer: ")


if input_value.isdigit():
    obj = IntegerPalindrome(int(input_value))
else:
    obj = StringPalindrome(input_value)

result = check_palindrome(obj)
print(result)
