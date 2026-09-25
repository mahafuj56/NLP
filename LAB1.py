import string

text = input("Enter a text: ")

text = text.lower()

result = text.translate(
    str.maketrans('', '', string.punctuation)
)

print("Output:", result)