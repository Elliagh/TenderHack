import pandas as pd
import chardet
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

with open('Resources\Logs.csv', 'rb') as f:
    enc = chardet.detect(f.read())
columns = ["id", "create_date", "log"]
data = pd.read_csv('Resources\Logs.csv', encoding = enc['encoding'], delimiter=";", usecols=columns)
nltk.download("stopwords") # поддерживает удаление стоп-слов
nltk.download('punkt') # делит текст на список предложений
nltk.download('wordnet') # проводит лемматизацию
from nltk.corpus import stopwords
data['log'][31]
new_log = []
lemmatize = nltk.WordNetLemmatizer()
for text_line in data['log']:
    text = nltk.word_tokenize(text_line)
    text = [lemmatize.lemmatize(word) for word in text_line]
    text = "".join(text)
    new_log.append(text)
count = CountVectorizer()
values = count.fit_transform(new_log).toarray()

print(values[0])
model = KMeans(n_clusters=19)
model.fit(values)
print(model.labels_)
print(model.cluster_centers_)