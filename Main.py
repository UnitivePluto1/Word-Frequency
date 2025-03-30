# Importing requests, BeautifulSoup and nltk
import requests
from bs4 import BeautifulSoup
import nltk


#We'll scrape the ebook Tales from the Hindu Dramatists by R. N. Dutta from the website Project Gutenberg (which contains a large corpus of books) using the Python package requests.
#Then we'll extract words from this web data using BeautifulSoup.
#Finally, we'll dive into analyzing the distribution of words using the Natural Language ToolKit (nltk).

#To analyze Hindu Dramatists, we need to get the contents of the eBook from somewhere.
#Luckily, the text is freely available online at Project Gutenberg as an HTML file: https://www.gutenberg.org/cache/epub/18285/pg18285-images.html

# Getting the Moby Dick HTML 
r = requests.get('https://www.gutenberg.org/cache/epub/18285/pg18285-images.html')

# Setting the correct text encoding of the HTML page
r.encoding = 'utf-8'

# Extracting the HTML from the request object
html = r.text

# Printing the first 2000 characters in html
#print(html[:2000])

# Creating a BeautifulSoup object from the HTML
soup = BeautifulSoup(html, 'html.parser')

# Getting the text out of the soup
text = soup.get_text()

# Printing out text between characters 2000-and-5000
#print(text[2000:5000])

# Creating a tokenizer
tokenizer = nltk.tokenize.RegexpTokenizer('\w+')

# Tokenizing the text
tokens = tokenizer.tokenize(text)

# Printing out the first 8 words / tokens 
print(tokens[:8])

# A new list to hold the lowercased words
words = []

# Looping through the tokens and make them lower case
for word in tokens:
    words.append(word.lower())

# Printing out the first 8 words / tokens 
print(words[:8])

nltk.download('stopwords')

# Getting the English stop words from nltk
sw = nltk.corpus.stopwords.words('english')

# Printing out the first eight stop words
print(sw[:8])
#print(sw)

# A new list to hold the Hindu Dramatists with No Stop words
words_ns = []

# Appending to words_ns all words that are in words but not in sw
for word in words:
    if word not in sw:
        words_ns.append(word)

# Printing the first 5 words_ns to check that stop words are gone
print(words_ns[:5])

# This command display figures inline
import matplotlib.pyplot as plt


# Creating the word frequency distribution
freqdist = nltk.FreqDist(words_ns)

# Plotting the word frequency distribution
freqdist.plot(25)
plt.show()

# What's the most common word in the Hindu Dramatists?
most_common_word = "King"
print("The most common word is: ", most_common_word)