try:
    # Taking input from the user for test marks
    test1 = float(input("Enter marks for Test 1: "))
    test2 = float(input("Enter marks for Test 2: "))
    test3 = float(input("Enter marks for Test 3: "))

    # Calculating the average marks for each test combination
    average1 = (test1 + test2) / 2
    average2 = (test2 + test3) / 2
    average3 = (test1 + test3) / 2

    # Finding the best average
    best_average = max(average1, average2, average3)

    # Printing the best average
    print("The best average marks out of the three tests are:", best_average)

except ValueError:
    print("Invalid input. Please enter numeric values for test marks.")
print("hello")
