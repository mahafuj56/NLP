import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download required NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Input text
text = input("Enter a text: ")

# Tokenize the text
words = word_tokenize(text)

# Create WordNetLemmatizer object
lemmatizer = WordNetLemmatizer()

# Apply lemmatization
lemmatized_words = []

for word in words:
    lemma = lemmatizer.lemmatize(word)
    lemmatized_words.append(lemma)

# Display output
print("\nOriginal Words:")
print(words)

print("\nLemmatized Words:")
print(lemmatized_words)