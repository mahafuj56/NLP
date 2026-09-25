import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

# Download required NLTK data
nltk.download('punkt')
nltk.download('punkt_tab')

# Input paragraph
paragraph = input("Enter a paragraph: ")

# Sentence tokenization
sentences = sent_tokenize(paragraph)

print("\nSentences:")
for i, sentence in enumerate(sentences, 1):
    print(i, ":", sentence)

# Word tokenization
words = word_tokenize(paragraph)

print("\nWords:")
print(words)