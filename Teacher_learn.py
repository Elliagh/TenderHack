import pandas as pd
from nltk.corpus import stopwords
import chardet
import nltk
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

with open('Resources\Logs.csv', 'rb') as f:
    enc = chardet.detect(f.read())
columns = ["id", "create_date", "log", "classification"]
data = pd.read_csv('Resources\Logs.csv', encoding = enc['encoding'], delimiter=";", usecols=columns)
nltk.download("stopwords") # поддерживает удаление стоп-слов
nltk.download('punkt') # делит текст на список предложений
nltk.download('wordnet') # проводит лемматизацию

count = CountVectorizer()
values = count.fit_transform(data["classification"]).toarray()

X = values
Y = data["classification"]





def methods_learn(X,Y, randomstate):
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, random_state = randomstate)
    nb = GaussianNB()
    result_bayes = nb.fit(x_train, y_train)
    logreg = LogisticRegression()
    result_logreg = logreg.fit(x_train, y_train)
    metodsvm = svm.SVC()
    result_svm = metodsvm.fit(x_train, y_train)
    return [nb.score(x_test,y_test), logreg.score(x_test,y_test), metodsvm.score(x_test,y_test)]

result = []
for i in range(1, 10):
    results = methods_learn(X,Y,i)
    print(f"progress:{i}")
    result.append(results)

res_baues = []
res_log_reg = []
res_svm = []

for res in result:
    res_baues.append(res[0])
    res_log_reg.append(res[1])
    res_svm.append(res[2])


plt.subplot(2, 2, 1)
plt.title("Наивный Байес")
plt.plot(res_baues)

plt.subplot(2, 2, 2)
plt.title("Логистическая регрессия")
plt.plot(res_log_reg)

plt.subplot(2, 2, 3)
plt.title("Опорный вектора")
plt.plot(res_log_reg)

plt.show()


