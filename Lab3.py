import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Download required NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

# Input text
text = input("Enter a text: ")

# Tokenize the text
words = word_tokenize(text)

# Get English stopwords
stop_words = set(stopwords.words('english'))

# Remove stopwords
filtered_words = []

for word in words:
    if word.lower() not in stop_words:
        filtered_words.append(word)

# Display output
print("\nOriginal Words:")
print(words)

print("\nAfter Removing Stopwords:")
print(filtered_words)