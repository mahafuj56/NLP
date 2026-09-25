import nltk
from nltk.tokenize import word_tokenize
from nltk.util import bigrams

# Download required NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')

# Input text
text = input("Enter a text: ")

# Tokenize the text
words = word_tokenize(text)

# Generate bigrams
bigram_list = list(bigrams(words))

# Display bigrams
print("\nBigrams:")
for bigram in bigram_list:
    print(bigram)