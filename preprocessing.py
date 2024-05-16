# Import libraries
import numpy as np
import pandas as pd
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
nltk.download('stopwords')
# Function for preprocessing texual data
def preprocessing(text):
    ''' input a string and it will return same string removing punctuations, stopwords, stemming and conversion into lowercase '''
    stemmer = SnowballStemmer(language='english') # creating object of SnowballStemmer
    text = ''.join([t for t in text if t not in string.punctuation]) # Remove punctuations
    text = [stemmer.stem(t.lower()) for t in text.split() if t not in stopwords.words('english')] # Stemming, Remove stopwords, lowercase
    text = [t for t in text if t.isnumeric()==False] # Remove numerical values and transform into lowercase
    return ' '.join(text)