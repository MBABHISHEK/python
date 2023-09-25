def isphonenumber(text):
    
    if len(text) != 12:
        return False
    
    for i in range(0, 3):
        if not text[i].isdigit():
            return False
   
    if text[3] != '-':
        return False
    
    for i in range(4, 7):
        if not text[i].isdigit():
            return False
    
    
   
    if text[7] != '-':
        return False
    
    for i in range(8, 12):
        if not text[i].isdigit():
            return False
    
    return True

import re

def isphonenumber_regex(text):
   
    pattern = r'\d{3}-\d{3}-\d{4}'
    
    match = re.search(pattern, text)
    if match:
        return True
    else:
        return False


text = input("Enter a phone number (format: XXX-XXX-XXXX): ")

if isphonenumber(text):
    print("Pattern recognized without regular expression.")
else:
    print("Pattern not recognized without regular expression.")


if isphonenumber_regex(text):
    print("Pattern recognized using regular expression.")
else:
    print("Pattern not recognized using regular expression.")
