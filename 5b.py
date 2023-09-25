import re

def extract_patterns(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

        phone_numbers = re.findall(r'\+\d{12}\b', text)

        email_addresses=re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text)

        return phone_numbers, email_addresses

def display_results(phone_numbers, email_addresses):
    print("Phone Numbers:")
    for number in phone_numbers:
        print(number)

    print("\nEmail Addresses:")
    for email in email_addresses:
        print(email)

file_path = 'sample.txt'

phone_numbers, email_addresses = extract_patterns(file_path)

display_results(phone_numbers, email_addresses)
