def read_file(filename):
    with open(filename, 'r') as file:
        return file.readlines()

def display_first_N_lines(lines, N):
    print(f"Displaying the first {N} lines of the file:")
    for line in lines[:N]:
        print(line.strip())

def count_word_occurrence(lines, word):
    word_count = 0
    for line in lines:
        words = line.strip().split()
        word_count += words.count(word)
    return word_count

filename = input("Enter the file name: ")
try:
    lines = read_file(filename)
    if lines:
        N = int(input("Enter the number of lines to display: "))
        display_first_N_lines(lines, N)
        word = input("Enter the word to find its frequency: ")
        frequency = count_word_occurrence(lines, word)
        print(f"The word '{word}' occurs {frequency} times in the file.")
    else:
        print("The file is empty or does not exist.")
except FileNotFoundError:
    print("File not found. Please enter a valid file name.")
