#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import chardet


# In[2]:


import nltk
import re


# In[3]:


with open(r'c:\Logs.csv', 'rb') as f:
    enc = chardet.detect(f.read())


# In[4]:


enc


# In[5]:


columns = ["id", "create_date", "log"]
data = pd.read_csv(r'c:\Logs.csv', encoding = enc['encoding'], delimiter=";", usecols=columns)


# In[6]:


nltk.download("stopwords") # поддерживает удаление стоп-слов
nltk.download('punkt') # делит текст на список предложений
nltk.download('wordnet') # проводит лемматизацию
from nltk.corpus import stopwords


# In[7]:


data


# In[8]:


data['log'][31]


# In[9]:


new_log = []
lemmatize = nltk.WordNetLemmatizer()
for text_line in data['log']:
    text = nltk.word_tokenize(text_line)
    text = [lemmatize.lemmatize(word) for word in text_line]
    text = "".join(text)
    new_log.append(text)


# In[10]:


new_log


# In[11]:


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer


# In[12]:


count = CountVectorizer()


# In[13]:


values = count.fit_transform(new_log).toarray()


# In[14]:


import numpy as np


# In[15]:


tokens={
    "verification": "verification",
    "invalid": "verification",
    "validate": "verification",
    "task": "handle exception error",
    "opcomplete":"handle exception error",
    "job error":"handle exception error",
    "error occurred": "handle exception error",
    "unexpected error":"handle exception error",
    "exception": "handle exception error",
    "method": "handle exception error",
    "ошибка": "handle exception error",
    "execution": "handle exception error",
    "unable": "handle exception error",
    "unhandled": "handle exception error",
    "request": "database",
    "query": "database",
    "get": "database",
    "delete": "database",
    "from": "database",
    "select": "database",
    "where": "database",
    "connection": "database",
    "database": "database",
    "nhibernate": "database",
    "documents": "database",
    "file storage": "database",
    "disk": "database",
    "file": "database",
    "data": "database",
    "данные": "database",
    "пакет": "database",
    "загрузка": "database",
    "загрузился": "database",
    "Timeout": "timeout",
    "time out": "timeout",
    "denied":"access",
    "не разрешено": "access",
    "already": "obj already added",
    "rabbitmq": "broker",
    "pp3": "broker",
    "not found": "not found",
    "не найдено": "not found",
    "не найден": "not found",
    "не найдена": "not found",
    "не удалось считать": "not found",
    "капча": "captcha",
    "капчи": "captcha",
    "capha": "captcha",
    "import": "import",
    "реиндексация":"database",
    "подписание по старому сертификату":"obsolete data",
    "не удалось скачать":"not found",
    "timed out":"timeout"
}
list_of_log_types = [
    "verification",
    "handle exception error",
    "database",
    "timeout",
    "access",
    "obj already added",
    "broker",
    "not found",
    "captcha",
    "import",
]


# In[16]:


values


# In[17]:


types = []
not_found_str = []
for text_line in data['log']:
    exist_token = False
    text_line = text_line.lower()
    dict_token = {}
    for token in tokens:
        if token in text_line:
            exist_token = True
            types.append(tokens[token])
            break
    if exist_token == False:
        print(text_line)


# In[18]:


values


# In[19]:


from sklearn.naive_bayes import GaussianNB


# In[20]:


from sklearn.model_selection import train_test_split


# In[21]:


X = values
Y = types


# In[22]:


x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.25, random_state = 25)


# In[23]:


nb = GaussianNB()


# In[24]:


result_bayes = nb.fit(x_train, y_train)


# In[25]:


print(nb.score(x_test,y_test))


# In[26]:


from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
result_logreg = logreg.fit(x_train, y_train)
print(logreg.score(x_test,y_test))


# In[27]:


from sklearn import svm
metodsvm = svm.SVC()
result_svm = metodsvm.fit(x_train, y_train)
print(metodsvm.score(x_test, y_test))


# In[ ]:




