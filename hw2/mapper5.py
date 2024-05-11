import sys
import io
import re
import nltk

nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stop_words = set(stopwords.words('english'))
punctuations = "!()-[]{};:'\',<>./?@#$%^&*_~"
stemmer = PorterStemmer()

def clean_text(text):
    text = text.strip()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = text.lower()
    for x in text:
        if x in punctuations:
            text = text.replace(x, " ")
    return text

input_stream = io.TextIOWrapper(sys.stdin.buffer, encoding='latin1')

docid = 1
for line in input_stream:
    line = clean_text(line)
    words = line.split()
    for word in words:
        word = stemmer.stem(word)
        if word not in stop_words:
            print('%s %s %s' % (word, 1, docid))
    docid +=1 