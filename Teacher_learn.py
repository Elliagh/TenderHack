import pandas as pd
import chardet
import nltk
from Helpers import Tokens as tokens
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
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
count = CountVectorizer()
values = count.fit_transform(new_log).toarray()
import numpy as np
types = []
not_found_str = []
for text_line in data['log']:
    exist_token = False
    text_line = text_line.lower()
    dict_token = {}
    for token in tokens.tokens:
        if token in text_line:
            exist_token = True
            types.append(tokens.tokens[token])
            break
    if exist_token == False:
        print(text_line)
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
X = values
Y = types
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 38)
nb = GaussianNB()
result_bayes = nb.fit(x_train, y_train)
print(nb.score(x_test,y_test))
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
result_logreg = logreg.fit(x_train, y_train)
print(logreg.score(x_test,y_test))
from sklearn import svm
metodsvm = svm.SVC()
result_svm = metodsvm.fit(x_train, y_train)
print(metodsvm.score(x_test, y_test))