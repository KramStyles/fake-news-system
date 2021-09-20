import numpy as np
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

from os import path

# data = pd.read_csv(path.join('assets/files', 'news1000.csv'))
# data = pd.read_csv(path.join('assets/files', 'news.csv'))
data = pd.read_excel(path.join('assets/files', 'news1000.xlsx'))
print(data.shape) # Number of rows and columns
print(data.head())
