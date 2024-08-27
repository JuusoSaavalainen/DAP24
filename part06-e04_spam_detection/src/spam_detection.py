#!/usr/bin/env python3

import numpy as np
import pandas as pd
import gzip
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


def spam_detection(random_state=0, fraction=1.0):
    with gzip.open("src/ham.txt.gz", "rb") as f:
        lines = f.readlines()
        ham = lines[:int(len(lines) * fraction)]
        ham = np.array(ham)
    with gzip.open("src/spam.txt.gz", "rb") as f:
        lines = f.readlines()
        spam = lines[:int(len(lines) * fraction)]
        spam = np.array(spam)

    X = np.concatenate([ham, spam])
    X = CountVectorizer().fit_transform(X)
    y = np.concatenate([np.zeros(ham.shape[0]), np.ones(spam.shape[0])])
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, random_state=random_state)

    model = MultinomialNB()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return accuracy, len(y_test), len(y_test) - accuracy * len(y_test)


def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")


if __name__ == "__main__":
    main()
