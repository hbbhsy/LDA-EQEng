# Import libraries
import numpy as np
import pandas as pd
import string
import sys
import os
import boto3
from os import listdir
from os.path import isfile, join
import unicodedata

# NLP
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer


#Loading Data From s3





if __name__ == '__main__':