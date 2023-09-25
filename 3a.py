def count_chars(sentence):
    word_count = len(sentence.split())
    digit_count = sum(1 for char in sentence if char.isdigit())
    uppercase_count = sum(1 for char in sentence if char.isupper())
    lowercase_count = sum(1 for char in sentence if char.islower())

    return word_count, digit_count, uppercase_count, lowercase_count

sentence = input("Enter a sentence: ")

word_count,digit_count,uppercase_count,lowercase_count=count_chars(sentence)

print("Number of words:", word_count)
print("Number of digits:", digit_count)
print("Number of uppercase letters:", uppercase_count)
print("Number of lowercase letters:", lowercase_count)
