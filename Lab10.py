import nltk
from nltk.tokenize import word_tokenize

# Download required NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')

# Input text
text = input("Enter a sentence: ")

# Tokenize the text
words = word_tokenize(text)

# Perform POS tagging
pos_tags = nltk.pos_tag(words)

# Perform Named Entity Recognition and chunking
tree = nltk.ne_chunk(pos_tags)

# Display the result
print("\nNamed Entities and Chunks:")
print(tree)