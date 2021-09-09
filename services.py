
from datetime import datetime
import pickle
import pandas as pd
from urllib.request import urlopen
from sklearn.linear_model import LogisticRegression
import numpy as np

vectorizer = None
model = None


url = 'https://drive.google.com/file/d/1qgStDGUiCg_WHlpDVKq4JK7hBE0hvmne/view?usp=sharing'
url2 = 'https://drive.google.com/uc?id=' + url.split('/')[-2]
sample = pd.read_csv(url2)

x = sample["comment_text"]
y = sample["target"]

pklurl = 'https://drive.google.com/file/d/14IJybVLp0C6rnuMKK4FifFYEEWNdrP89/view?usp=sharing'
pklurl2 = 'https://drive.google.com/uc?id=' + pklurl.split('/')[-2]
filename = pklurl2

with urlopen(filename) as f:
    vectorizer, model = pickle.load(f)
print("initialized model")

def calculateScore(ipt):
    print(ipt["email"])
    logReg = LogisticRegression()

    logReg.classes_ = np.asarray(ipt["classes_"], dtype=np.float32)
    logReg.coef_ = np.asarray(ipt["coef_"], dtype=np.float32)
    logReg.intercept_ = np.asarray(ipt["intercept_"], dtype=np.float32)
    logReg.n_iter_ = np.asarray(ipt["n_iter_"], dtype=np.float32)

    score = logReg.score(vectorizer.transform(x), y)
    print(score)
    return score    





