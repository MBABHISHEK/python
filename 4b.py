def roman_to_integer(roman_numeral):
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    i = 0  # Initialize the index for iteration

    while i < len(roman_numeral):
        # Get the integer value of the current Roman numeral character
        value = roman_dict[roman_numeral[i]]

        # Check for multi-character subtraction cases
        if i + 1 < len(roman_numeral) and roman_dict[roman_numeral[i + 1]] > value:
            result += roman_dict[roman_numeral[i + 1]] - value
            i += 2  # Skip the next character since it's already accounted for
        else:
            result += value
            i += 1  # Move to the next character

    return result
def main():
    # Get the Roman numeral input from the user
    roman_numeral = input("Enter a Roman numeral: ")
    
    try:
        # Call the function to convert the Roman numeral to an integer value
        integer_value = roman_to_integer(roman_numeral.upper())
        
        # Display the result
        print("The integer value of {} is: {}".format(roman_numeral.upper(), integer_value))

    except KeyError:
        print("Invalid Roman numeral. Please enter a valid Roman numeral.")

if __name__ == "__main__":
    main()