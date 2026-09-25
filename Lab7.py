import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# Download required NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')

# Input text
text = input("Enter a text: ")

# Tokenize the text
words = word_tokenize(text)

# Create frequency distribution
fdist = FreqDist(words)

# Display most frequent words
print("\nMost Frequent Words:")

for word, frequency in fdist.most_common(10):
    print(word, "->", frequency)