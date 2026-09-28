# Palindrome Checker

text = input("Enter a word or sentence: ")

# Normalize the input
normalized_text = text.replace(" ", "").lower()

# Check whether the input is a palindrome
if normalized_text == normalized_text[::-1]:
    print("The given input is a palindrome.")
else:
    print("The given input is not a palindrome.")