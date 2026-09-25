import nltk 
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
 
# Download required NLTK resources 
nltk.download('punkt') 
nltk.download('punkt_tab') 
 
# Input text 
text = input("Enter a text: ") 
 
# Tokenize the text 
words = word_tokenize(text) 
 
# Create PorterStemmer object 
stemmer = PorterStemmer() 
 
# Apply stemming 
stemmed_words = [] 
 
for word in words: 
    stemmed_word = stemmer.stem(word) 
    stemmed_words.append(stemmed_word) 
 
# Display output 
print("\nOriginal Words:") 
print(words) 
 
print("\nStemmed Words:") 
print(stemmed_words)