string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

similarity = sum(a == b for a, b in zip(string1, string2)) / max(len(string1), len(string2))

print("Original string:")
print(string1)
print(string2)
print("Similarity between two said strings:")
print(similarity)
