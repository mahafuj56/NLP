import nltk
from nltk.tokenize import word_tokenize

# Download required NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

# Input sentence
sentence = input("Enter a sentence: ")

# Tokenize the sentence
words = word_tokenize(sentence)

# Perform POS tagging
pos_tags = nltk.pos_tag(words)

# Display POS tags
print("\nPOS Tagged Words:")

for word, tag in pos_tags:
    print(word, "->", tag)